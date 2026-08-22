/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // خروجی standalone برای استقرار سبک در Docker/سرور
  output: 'standalone',
  i18n: {
    // بدون i18n؛ فقط فارسی
    locales: ['fa'],
    defaultLocale: 'fa',
  },
  images: {
    // تصاویر از وردپرس (دامنه متغیر) — برای سادگی، loader پیش‌فرض
    remotePatterns: [
      { protocol: 'https', hostname: '**' },
      { protocol: 'http', hostname: '**' },
    ],
    unoptimized: true,
  },
};

module.exports = nextConfig;
