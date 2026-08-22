import Head from 'next/head';
import '../styles/globals.css';

export default function App({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>استودیو اثر | هم مسیر تا تغییر</title>
        <meta
          name="description"
          content="استودیو اثر: خدمات حرفه‌ای تولید محتوا، طراحی سایت، طراحی اپلیکیشن، طراحی لوگو، طراحی هویت برند و طراحی‌های چاپی"
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <Component {...pageProps} />
    </>
  );
}
