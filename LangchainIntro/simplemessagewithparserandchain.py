# simplemessagewithparserandchain.py

def parse_message(msg):
    return msg.upper()

def chain_message(msg):
    parsed = parse_message(msg)
    return f"[CHAINED] {parsed}"

if __name__ == "__main__":
    print(chain_message("Hello from Langchain!")) 