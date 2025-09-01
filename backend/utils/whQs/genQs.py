# uv run -m utils.whQs.genQs
from lib.openai import openai_client
from pydantic import BaseModel

class WhQs(BaseModel):
    scene_description: str
    who: str
    what: str
    when: str
    where: str
    why: str
    how: str

base_prompt = """
You are a speech pathologist with 30 years of experience.
In the style of Hans Christian Andersen, describe a scene featuring a main character. The scene should be max 3 sentences long.
After that create six short WH-questions (Who, What, When, Where, Why, How) based on the scene.
The scene should have one main character and all of the six short WH-questions should relate to the main character.
The scene and questions should be suitable for a {age}-year-old child. Keep the language simple and easy for a {age}-year-old child to understand.
The scene is going to be read to a child who has the following interests: {interests}.
Make the scene and questions relevant to the child's interests.
"""

def create_prompt(age: int, interests: str):
    return base_prompt.format(age=age, interests=interests)

def gen_qs(age: int, interests: str):
    system_prompt = create_prompt(age, interests)
    
    response = openai_client.responses.parse(
        model="gpt-5",
        reasoning={"effort": "minimal"},
        input=[{"role": "system", "content": system_prompt}],
        text_format=WhQs,
    )
    return {
        "scene_description": response.output_parsed.scene_description,
        "who": response.output_parsed.who,
        "what": response.output_parsed.what,
        "when": response.output_parsed.when,
        "where": response.output_parsed.where,
        "why": response.output_parsed.why,
        "how": response.output_parsed.how,
    }

if __name__ == "__main__":
    age = 5
    # interests = "princesses, unicorns, swimming, pancakes, singing"
    interests = "tractors, cows, horses, mud, dinosaurs"
    # interests = "drawing, singing, cherry blossoms, cats, sushi"
    # interests = "soccer, superheroes, volcanoes, dogs, cars"
    # interests = "ballet, painting, rabbits, fairies, chocolate"
    
    print(gen_qs(age, interests))