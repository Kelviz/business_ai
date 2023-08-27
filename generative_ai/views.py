from django.shortcuts import render
import openai

def generate_business_idea():
    industry = input("industry: ")
    audience = input("target audience: ")
    budget = input("budget: ")
    txt = f'Business ideas about {industry} targeting {audience}
    with the budget of {budget}.'

    openai.api_key="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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {
          "role": "system",
          "content": "Generate"
        },
        {
      "role": "user",
      "content":txt
        }
      ],
       temperature=0,
       max_tokens=1024,
       top_p=1,
       frequency_penalty=0,
       resence_penalty=0

      )

   ideas = response['choices'][0]['message']['content']

   print(ideas)

ideas()
