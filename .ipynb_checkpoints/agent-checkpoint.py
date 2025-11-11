# from openai import OpenAI
# from colorama import Fore, Style, init
 
# # Initialize colorama
# init(autoreset=True)
# # Set up client
# openai_api_key = "EMPTY"  
# openai_api_base = "http://cmi-dgx-station-5.tail69783d.ts.net:8081/v1"
# client = OpenAI(
#     api_key=openai_api_key,
#     base_url=openai_api_base,
# )
 
# # Initialize message history
# messages = [
#     {"role": "system", "content": "You are a helpful assistant."}
# ]
# print("Start chatting with the assistant! Type 'exit' or 'quit' to end.\n")
# while True:
#     user_input = input(f"{Fore.BLUE}User: {Style.RESET_ALL}")
#     if user_input.strip().lower() in ["exit", "quit"]:
#         print("Exiting chat. Goodbye!")
#         break
#     messages.append({"role": "user", "content": user_input})
#     chat_response = client.chat.completions.create(
#         model="meta-llama/Meta-Llama-3-8B-Instruct",
#         messages=messages,
#         stream=True,
#         max_tokens=2048,
#         temperature=0.7,
#     )
   
#     print(f"{Fore.GREEN}Assistant: {Style.RESET_ALL}", end="", flush=True)
#     assistant_message = ""
 
#     for event in chat_response:
#         # Each event contains incremental content
#         delta = event.choices[0].delta.content
#         if delta:
#             print(Fore.GREEN + delta + Style.RESET_ALL, end="", flush=True)
#             assistant_message += delta
 
#     print("\n")  # Newline after full message
#     messages.append({"role": "assistant", "content": assistant_message})
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from colorama import Fore, Style, init
 
# Initialize colorama for colored output
init(autoreset=True)
 
# # Configure ChatOpenAI to use vLLM server
# chat = ChatOpenAI(
#     model="Qwen/Qwen2.5-7B-Instruct",  # match the model served by vLLM
#     api_key="EMPTY",  # vLLM ignores API key, but ChatOpenAI requires one
#     base_url="http://cmi-dgx-station-5.tail69783d.ts.net:8081/v1",
#     temperature=0.7,
#     max_tokens=1024,
#     streaming=True,  # enable streaming output
# )
from langchain_community.llms import VLLM
from langchain_openai import ChatOpenAI
 
# Use vLLM as backend with OpenAI-compatible API
chat = ChatOpenAI(
    base_url="http://research-ai.tail69783d.ts.net:8001/v1",
    api_key="EMPTY",
    model="openai/gpt-oss-20b",
    temperature=0,
    max_completion_tokens=10000
)
 
# Chat history
messages = [
    SystemMessage(content="You are a helpful assistant.")
]
 
print("Start chatting with the assistant! Type 'exit' or 'quit' to end.\n")
 
while True:
    user_input = input(f"{Fore.BLUE}User: {Style.RESET_ALL}")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Exiting chat. Goodbye!")
        break
 
    messages.append(HumanMessage(content=user_input))
 
    print(f"{Fore.GREEN}Assistant: {Style.RESET_ALL}", end="", flush=True)
    assistant_message = ""
 
    # Stream the response from ChatOpenAI
    for chunk in chat.stream(messages):
        if chunk.content:
            print(Fore.GREEN + chunk.content + Style.RESET_ALL, end="", flush=True)
            assistant_message += chunk.content
 
    print("\n")  # newline after assistant finishes
    messages.append(SystemMessage(content=assistant_message))