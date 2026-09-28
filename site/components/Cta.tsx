export default function Cta() {
  const steps = [
    {
      title: '01 Select what you need guidance on.',
      desc: 'Choose from Love & Relationships, Past Life, Dream Meaning, or Angel Numbers.',
    },
    {
      title: "02 Tell us what's on your mind.",
      desc: "Share your question and, where needed, provide your birth details, palm photo, face photo, or any additional information to help.",
    },
    {
      title: '03 Expert guidance, personalized for you.',
      desc: 'Our experienced astrologers carefully study your information using birth charts, palm reading, face reading, energy analysis, etc.',
    },
    {
      title: '04 Get your personalized insights.',
      desc: 'Receive a detailed reading with meaningful insights, guidance, and practical next steps to help you move forward with clarity.',
    },
  ];
  return (
    <section className="py-12 bg-[#080625] text-[#ffffff] font-[Inter,ui-serif]">
      <div className="max-w-5xl mx-auto px-4 text-center">
        <h2 className="text-2xl md:text-3xl font-bold mb-2">How It Works</h2>
        <p className="mb-8">Get personalized spiritual guidance in four simple steps.</p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {steps.map((step, i) => (
            <div key={i} className="bg-[#080625]/60 p-4 rounded-lg hover:bg-[#080625]/80 transition">
              <h3 className="font-semibold mb-2">{step.title}</h3>
              <p className="text-sm">{step.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
