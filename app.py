from bs4 import BeautifulSoup
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

html_file = os.path.join(script_dir, "index.html")

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "lxml")

questions = soup.select("div.que")

output_file = os.path.join(script_dir, "izvoz_vprasanja.txt")

with open(output_file, "w", encoding="utf-8") as out:

    for idx, question_div in enumerate(questions, start=1):

        question_text_tag = question_div.select_one("div.qtext p")
        
        correct_answer_tag = question_div.select_one("div.outcome .rightanswer")
        
        if question_text_tag and correct_answer_tag:
            question_text = question_text_tag.get_text(strip=True)
            correct_answer_text = correct_answer_tag.get_text(strip=True)
            
            if "Pravilni odgovor je:" in correct_answer_text:
                correct_answer_text = correct_answer_text.split("Pravilni odgovor je:")[-1].strip()
            
            out.write(f"Vprašanje {idx}: {question_text}\n")
            out.write(f"Odgovor: {correct_answer_text}\n\n")
    
print(f"Končano! Rezultati so zapisani v datoteko: {output_file}")
