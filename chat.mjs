import { GoogleGenerativeAI } from "@google/generative-ai";
import readline from "readline";
const genAI = new GoogleGenerativeAI("TON_API_KEY_ICI");
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
async function ask() {
  rl.question("Vous: ", async (input) => {
    if (input.toLowerCase() === "exit") return rl.close();
    try {
        const result = await model.generateContent(input);
        console.log("\nGemini:", result.response.text(), "\n");
    } catch (e) { console.error("\nErreur:", e.message); }
    ask();
  });
}
console.log("Connecté. Tapez 'exit' pour quitter.");
ask();
