#!/usr/bin/env python3
"""
A simple interactive prompt utility
"""

def main():
    """Main function to run the interactive prompt"""
    print("Welcome to Kosen Shirabasu Maru Wakari Tarou Prompt!")
    print("Type 'exit' to quit")
    print()
    
    while True:
        try:
            user_input = input("prompt> ")
            
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            
            if user_input:
                print(f"You entered: {user_input}")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
