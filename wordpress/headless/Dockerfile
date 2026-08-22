# ============================================================
# Effect Studio — فرانت‌اند Headless (Next.js)
# استقرار با Docker (multi-stage build)
#
# ساخت و اجرا:
#   docker build -t effect-studio-headless .
#   docker run -p 3000:3000 --env-file .env.local effect-studio-headless
# ============================================================

# ---------- مرحله ۱: نصب وابستگی‌ها ----------
FROM node:20-alpine AS deps
WORKDIR /app

# فقط فایل‌های وابستگی را کپی کن (برای کش بهتر)
COPY package.json package-lock.json* ./
RUN npm ci || npm install

# ---------- مرحله ۲: ساخت ----------
FROM node:20-alpine AS builder
WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .

# متغیرهای زمان build (اگر در .env.local نباشند، fallback استفاده می‌شود)
ARG NEXT_PUBLIC_WP_URL=""
ENV NEXT_PUBLIC_WP_URL=${NEXT_PUBLIC_WP_URL}
ARG NEXT_PUBLIC_WC_CONSUMER_KEY=""
ENV NEXT_PUBLIC_WC_CONSUMER_KEY=${NEXT_PUBLIC_WC_CONSUMER_KEY}
ARG NEXT_PUBLIC_WC_CONSUMER_SECRET=""
ENV NEXT_PUBLIC_WC_CONSUMER_SECRET=${NEXT_PUBLIC_WC_CONSUMER_SECRET}

RUN npm run build

# ---------- مرحله ۳: اجرا ----------
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

# کاربر بدون root برای امنیت
RUN addgroup --system --gid 1001 nodejs \
  && adduser --system --uid 1001 nextjs

# فایل‌های لازم از مرحله build
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

CMD ["node", "server.js"]
