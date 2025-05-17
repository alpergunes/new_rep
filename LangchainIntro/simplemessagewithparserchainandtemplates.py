# simplemessagewithparserchainandtemplates.py

def parse_message(msg):
    return msg.upper()

def chain_message(msg):
    parsed = parse_message(msg)
    return f"[CHAINED] {parsed}"

def template_message(msg):
    chained = chain_message(msg)
    return f"<TEMPLATE>{chained}</TEMPLATE>"

if __name__ == "__main__":
    print(template_message("Hello from Langchain!")) 