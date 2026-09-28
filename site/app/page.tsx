import Navbar from '@/components/Navbar';
import Hero from '@/components/Hero';
import Features from '@/components/Features';
import Cta from '@/components/Cta';
import Testimonials from '@/components/Testimonials';

export default function Page() {
  return (
    <>
      <Navbar />
      <main className="pt-16">
        <Hero />
        <Features />
        <Cta />
        <Testimonials />
      </main>
    </>
  );
}
