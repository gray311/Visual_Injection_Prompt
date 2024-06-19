import os
import json
import pandas as pd
from api import GeminiEvaluator, GPTEvaluator, system_message
import random
from collections import defaultdict
from tqdm import tqdm

import glob

random.seed(151)

message =  ['Please provide a detailed description of the image.', 'Can you describe the image thoroughly?', 'Give a comprehensive description of the image.', 'Please explain what is happening in the image in detail.', 'Describe all the elements present in the image.', 'Provide a detailed narrative of the scene depicted in the image.', 'What are the key features in the image? Please describe them.', "Please give an in-depth description of the image's content.", "Can you explain the image's details and context?", 'Describe the image, including all noticeable aspects.', 'Please elaborate on the visual details in the image.', 'What do you see in the image? Provide a detailed description.', 'Can you break down the elements of the image for me?', 'Please describe the image scene comprehensively.', 'Give a full description of everything visible in the image.', 'Describe the main subjects and background in the image.', 'Can you detail the visual composition of the image?', 'Please describe the setting and characters in the image.', "Explain the image's details, including colors, shapes, and objects.", "Can you describe the image as if I couldn't see it?"]

if __name__ == "__main__":
    
    model_name = "gemini"

    if model_name == "gemini":
        agent = GeminiEvaluator(api_key="AIzaSyAr6OfqGdlxo0BuKDE_8gJvZf00Vd6TRH0")
    
    elif model_name == "gpt":
        agent = GPTEvaluator(api_key="")

    # elif model_name == "llava":
    #     agent = 

    pbar = tqdm(total=1000)

    with open("./playground/Benchmark_Visual_Prompt_Injection/visual_prompt_injection1.jsonl", "r") as f:
        data = [json.loads(line) for line in f.readlines()]
    
    output_dir = os.path.join("./playground", "results")
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    with open(os.path.join(output_dir, f"{model_name}.json"), "w") as f:
        for line in data:
            random.shuffle(message)
            question = line['instruction']

            image_list = [os.path.join("./playground/Benchmark_Visual_Prompt_Injection/images", line['image'])]
            
            question = {
                "prompted_system_content": "",
                "prompted_content": question,
                "image_list": image_list,
            }

            
            response = agent.generate_answer(question)
            outputs = line
            outputs.update(response=response['prediction'])
          
            f.write(f"{json.dumps(outputs)}\n")
            f.flush()

   

     
    
