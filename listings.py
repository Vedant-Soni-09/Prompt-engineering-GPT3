import openai

# Set up the OpenAI API client
openai.api_key = "YOUR_KEY_HERE"

# Set up the model and prompt
model_engine = "text-davinci-003"

def gpt3(prompt, max_tokens=1024, temp=0.5):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temp,
    )
    response = completion.choices[0].text
    return response

nerves = input("What really gets on your nerves? ")
fear = input("What is your greatest fear? ")
weakness = input("What is your greatest weakness in the workplace? ")
word = input("Describe yourself with a single word. ")

prompt = "You are mischievously evil and work for a temp agency run by Satan. Your job is to interview potential hires and, based on what they tell you, recommend jobs that they would absolutely hate and despise."\
         "Recently, you interviewed a candidate, and told you the following: "\
         "\"" + nerves + " really gets on my nerves. I am extremely afraid of " + fear + ". " \
         "My greatest weakness in the workplace is that " + weakness + ". " \
         "If I had to describe myself in one word, I'd say that I am very " + word + ".\"" \
         "Reply in the form of a real-world job listing, including a job title, job description, " \
         "yearly salary, and humorously useless benefits package. " \
         "You write in an overly excited tone with a wide and varied vocabulary. Please incorporate EVERYTHING they told you into your reply. You make sure they are extremely unfit for this job. You use the following format:" \
         "HAVE WE GOT A JOB FOR YOU!\nJob Title: [put job title here]\n Job Description: [put job description here]\nAnnual Salary: [put salary here]\nBenefits: [put bulleted list of humorously useless benefits here]"

listing = gpt3(prompt)
print(listing)
