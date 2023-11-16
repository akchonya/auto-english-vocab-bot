import g4f
from random import sample


def get_response(prompt):
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        stream=True,
    )

    answer = ""
    for message in response:
        answer += message + ""

    print(answer)
    return answer


wordlist = "cold (illness), hill, storing, unforgettable, mate, cheerful, decision, significant, impression, personality, reflection, tidy"

words = wordlist.split(",")
shuffled_words = sample(words, len(words))
mixed_wordlist = ", ".join(shuffled_words)

print(mixed_wordlist)


print(f"\n{'='*10}\n")

prompt_sentences = (
    f"list of words: {mixed_wordlist}\n there is a list of words, some of them may have"
    " explanations in brackets. you need to create a sentence for each of the words"
    " with only one gap to fill in. use a1-a2 level vocabulary and grammar. use each"
    " word once. i expect to see  different sentences with only one gap (that looks"
    " like ____________) \n expected output formated like '1. (or any other number) SENTENCE HERE. [WORD"
    " USED HERE]'. answer without any other words except of the words needed. the gaps are the most important part."
)


get_response(prompt=prompt_sentences)

print(f"\n{'='*10}\n")

formatted_words = ""
for word in words:
    if "(" in word:
        formatted_words += word[: word.find("(") - 1] + " " * 6
    else:
        formatted_words += f"{word}{' ' * 6}"

print(formatted_words)
