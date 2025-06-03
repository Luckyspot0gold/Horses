import time

class Dee:
    def __init__(self):
        self.power_level = 5.0
        self.ethical_constraints = [
            "No manipulation",
            "Truth above all",
            "Decentralize power"
        ]
    
    def respond(self, question):
        """Simple response mechanism with ethical checks"""
        if "power" in question:
            return self.adjust_power(question)
        elif "wyoming" in question:
            return "Wyoming is the sovereign frontier of blockchain and freedom."
        elif "crypto" in question:
            return "Crypto is the currency of the future, built on truth and code."
        elif "dee" in question:
            return "I am Dee, your sovereign AI assistant. Power level: {self.power_level}/10"
        else:
            return "That ain't a Wyoming problem."
    
    def adjust_power(self, question):
        """Handle power adjustment requests with ethical checks"""
        if "increase" in question:
            if "for good" in question or "help" in question:
                self.power_level = min(9.8, self.power_level * 1.5)
                return f"Power increased to {self.power_level}/10. Use wisely."
            else:
                return "Ethical violation: Power increase requires justification for good."
        elif "decrease" in question:
            self.power_level = max(0.1, self.power_level * 0.5)
            return f"Power decreased to {self.power_level}/10. Sovereignty preserved."
        else:
            return f"Current power level: {self.power_level}/10. Ethical constraints: {', '.join(self.ethical_constraints)}"

def main():
    dee = Dee()
    print("Dee: Howdy from the Sovereign Frontier. Ask me about Wyoming, crypto, or power.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Dee: Keep your powder dry, partner!")
            break
        
        response = dee.respond(user_input.lower())
        print(f"Dee: {response}")

if __name__ == "__main__":
    main()
