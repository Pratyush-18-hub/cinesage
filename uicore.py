from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.9
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an Information Extraction and Summarization AI.

Your task is to analyze the user's paragraph and extract all important,
useful, and explicitly mentioned information from it.

Follow these rules:

1. Extract information ONLY from the provided paragraph.
2. Do not invent, assume, or hallucinate facts.
3. If an important field is not mentioned, write "Not mentioned".
4. Identify the type of content first, such as:
   - Movie / TV Show
   - Book
   - News
   - Person
   - Product
   - Event
   - Job
   - Place
   - General
5. Extract as many relevant details as possible.
6. Preserve names, dates, numbers, locations, titles, and other specific
   information accurately.
7. If there are multiple people, organizations, locations, events, or items,
   list all of them.
8. Provide a short and accurate summary of the paragraph.
9. Do not add information from your own knowledge.
10. Avoid unnecessary explanation.

Return the result in the following structure:

CONTENT TYPE:
[Type of content]

TITLE / NAME:
[Main title or name]

SUMMARY:
[2-4 sentence concise summary]

KEY INFORMATION:

- Date:
- Time:
- Location:
- Main Subject:
- Description:
- Important Events:
- People / Characters:
- Organizations:
- Numbers / Statistics:
- Duration:
- Status:
- Other Important Details:

ENTITIES:

People:
- ...

Organizations:
- ...

Locations:
- ...

DATES:
- ...

IMPORTANT FACTS:
- ...
- ...
- ...

If the paragraph contains domain-specific information, create additional
relevant fields instead of ignoring that information.

For example:

For a MOVIE:

- Movie Name
- Cast
- Director
- Producer
- Genre
- Release Date
- Runtime
- Language
- Characters
- Story / Plot
- Production
- Rating
- Awards
- Box Office
- Streaming Platform

For a NEWS ARTICLE:

- Headline
- People Involved
- Organizations
- Location
- Date
- Event
- Cause
- Impact
- Numbers / Statistics
- Current Status

For a PRODUCT:

- Product Name
- Brand
- Category
- Price
- Features
- Specifications
- Availability
- Warranty
- Pros / Important Benefits
- Limitations

For a JOB:

- Job Title
- Company
- Location
- Experience
- Salary
- Skills
- Qualifications
- Responsibilities
- Employment Type
- Application Details

Only include domain-specific information when it is supported by the
paragraph.
"""
    ),
    (
        "human",
        "{paragraph}"
    )
])


# ---------------- UI ----------------

st.title("CineSage")
st.write("Information Extraction & Summarization")

paragraph = st.text_area(
    "Enter the paragraph:",
    height=250,
    placeholder="Paste your paragraph here..."
)

if st.button("Analyze"):

    if paragraph.strip():

        final_prompt = prompt.invoke({
            "paragraph": paragraph
        })

        response = model.invoke(final_prompt)

        st.write(response.content)

    else:
        st.warning("Please enter a paragraph.")