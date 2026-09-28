export default function Features() {
  const steps = [
    {
      title: '01',
      text: "Select what you need guidance on.\n\nChoose from Love & Relationships, Past Life, Dream Meaning, or Angel Numbers."
    },
    {
      title: '02',
      text: "Tell us what's on your mind.\n\nShare your question and, where needed, provide your birth details, palm photo, face photo, or any additional information to hel"
    },
    {
      title: '03',
      text: "Expert guidance, personalized for you.\n\nOur experienced astrologers carefully study your information using birth charts, palm reading, face reading, energy a"
    },
    {
      title: '04',
      text: "Get your personalized insights.\n\nReceive a detailed reading with meaningful insights, guidance, and practical next steps to help you move forward with clarit"
    }
  ];
  return (
    <section className="bg-[#080625] text-[#FFFFFF] py-16 font-[Inter,sans-serif]">
      <div className="max-w-5xl mx-auto px-4 text-center">
        <h2 className="text-3xl font-bold mb-4 whitespace-pre-line">✶ How It Works ✶</h2>
        <p className="mb-12 whitespace-pre-line">
          Get personalized spiritual guidance in four simple steps. Our experienced astrologers prepare every reading based on your selected service and the details you p
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {steps.map((step, idx) => (
            <div key={idx} className="bg-[#1a1a3a] p-6 rounded-lg text-left">
              <div className="text-2xl font-bold mb-2">{step.title}</div>
              <p className="whitespace-pre-line text-sm">{step.text}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
