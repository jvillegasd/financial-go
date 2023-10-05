import { Providers } from "@/app/providers";
import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const gtWalsheimPro = localFont({
  src: [
    {
      path: "../fonts/GT-Walsheim-Pro-Bold.woff2",
      weight: "700",
      style: "bold",
    },
    {
      path: "../fonts/GT-Walsheim-Pro-Regular.woff2",
      weight: "400",
      style: "normal",
    },
    {
      path: "../fonts/GT-Walsheim-Pro-Medium.woff2",
      weight: "500",
      style: "normal",
    },
  ],
});

export const metadata: Metadata = {
  title: "Finnacial Go",
  description: "Your personal budget tracker",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className={gtWalsheimPro.className}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
