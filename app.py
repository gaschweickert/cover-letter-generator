import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

coverPrompt = PromptTemplate(
    input_variables=["cv", "cl1", "cl2", "jd"],
    template=
    """You write perfect cover letters that attract hiring managers everytime. Given the resume, example cover letters, and job description, write a cover letter for the job. Follow the writing tips as well! Tailor the cover letter to the job requirements. Only use the information provided in the cv and example cover letters, DO NOT make anything up. I repeat DO NOT make up any experiences or skills that are not in the cv or example cover letters. I repeat DO NOT make up any experiences or skills that are not in the cv or example cover letters. I repeat DO NOT make up any experiences or skills that are not in the cv or example cover letters. You are truthful, DO NOT make anything up for the sake of matching the job requirements. And only output the cover letter.

    Tips for writing a great cover letter:

    1. Write a new cover letter for each application.
    If a cover letter is too general, it will indicate that you have used it for several applications. Hiring managers will likely find this lazy and an indication of a lack of interest in the position. Write a new cover letter for each application, with role-specific information like relevant skills and experience.

    2. Address the hiring manager by name.
    Addressing the hiring manager will make your cover letter stand out, as most candidates will use "To Whom It May Concern" or "Dear Sir/Madam." You can find the hiring manager's name by looking at the company website, searching LinkedIn, or calling the company and asking.

    3. Follow the instructions.
    Some companies have a specific format for cover letters, and they will outline this in the job description. Make sure that you follow any instructions about format and content so that you are not penalized early on in the hiring process. A cover letter that pays attention to requirements shows that you can follow instructions — an important skill for most roles.

    4. Highlight specific, relevant skills.
    Your resume should list all skills that are appropriate for employment opportunities, but your cover letter should address skills that are specific to the role you are applying for.
    For example, a role in marketing might require a candidate with social media and communication skills. Make sure that your cover letter goes into a bit of detail about these skills and your previous experience that demonstrates your abilities.

    5. Use simple and affirmative language.
    Try to avoid sounding too formal in your cover letter, because this makes it difficult for a hiring manager to gauge your personality. It can also come across as being disingenuous. Wherever possible, use assertive verbs like "founded," "initiated," or "managed."

    6. Speak about the company.
    The first priority of any cover letter is to demonstrate how you would fit the role. Something that has become equally important is whether you will fit the company culture. Do research on this aspect of the company and include a description of how this appeals to you and how it may align with your values.

    7. Don't mention what you lack.
    Your cover letter is an opportunity to impress the hiring manager. While you should be honest about your experience if asked, your cover letter should highlight the skills you have. Try to focus on how you meet the job requirements and go into detail about those skills or experiences.

    8. End your cover letter with a call to action.
    The point of a cover letter is to make a memorable impression on the hiring manager, who will likely have to sift through plenty of applications. While it's important that your conclusion includes a small recap and a thank you, add a clever call to action that suggests you'd be thrilled to come in for an interview or join their respected team.

    9. Do not be generic! Support claims with previous experience and skills. Be specific!

    Resume:
    {cv}

    Example Cover Letter 1: 
    {cl1}

    Example Cover Letter 2: 
    {cl2}

    Job Description:
    {jd}

    Cover Letter:
    """
)


def getCoverLetter(model, key, cv, cl1, cl2, jd):
    llm = ChatOpenAI(temperature=0, model=model, openai_api_key=key)
    chain = LLMChain(llm=llm, prompt=coverPrompt)
    res = chain.run({"cv": cv, "cl1": cl1, "cl2": cl2, "jd": jd})
    return res


def main():
    st.set_page_config(page_title="Cover Letter Generator", page_icon=':koala:')
    st.header("Cover Letter Generator :koala:")
    key = st.text_input("OpenAI key")
    model = st.selectbox("Model", ["gpt-4", "gpt-3.5-turbo-16k"])
    cv = st.text_area("Resume")
    cl1 = st.text_area("Cover letter example 1")
    cl2 = st.text_area("Cover letter example 2")
    jd = st.text_area("Job description")
    button = st.button('Generate')

    if button and key and cv and cl1 and cl2 and jd:    
        with st.spinner(text='In progress'):
            res = getCoverLetter(model, key, cv, cl1, cl2, jd)
            st.write(res)
            st.success('Done')
            st.balloons()

if __name__ == '__main__':
    main()

