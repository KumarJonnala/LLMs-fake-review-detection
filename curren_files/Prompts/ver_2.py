class Config:

    file_path = ""

    model = ""

    zero_shot_prompt_template = """
    You are an expert at detecting fake and real reviews. Carefully analyze the following review for signs such as:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Repetitive or templated phrasing
    - Marketing-like wording or unnatural flow
    - Specific details vs. general statements
    Review: "{text}"
    Classify this review as either "real" or "fake" (respond with only one word):
    """

    # Define one-shot classification prompt with one example
    one_shot_prompt_template = """
    You are an expert at detecting fake and real reviews. Carefully analyze the following review for signs such as:
    Task: Classify the following review of a  Amazon product as either "real" or "fake". Carefully analyze the following review for signs such as:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Repetitive or templated phrasing
    - Marketing-like wording or unnatural flow
    - Specific details vs. general statements

    Example:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Classification: fake
    Now classify this review:
    Review: "{text}"
    Classify this review as either "real" or "fake" (respond with only one word):
    """
    
    # Define few-shot classification prompt with multiple examples
    few_shot_prompt_template = """
    You are an expert at detecting real and fake reviews.

   Task: Classify the following review of a  Amazon product as either "real" or "fake". Carefully analyze the following review for signs such as:
    - Overly generic or vague language
    - Exaggerated praise or criticism
    - Repetitive or templated phrasing
    - Marketing-like wording or unnatural flow
    - Specific details vs. general statements

    Here are some examples:

    Example 1:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Classification: fake
    Example 2:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands.
    Classification: real

    Example 3:
    Review: "I had a 3 piece blue set of this luggage and on a trip recent trip the largest piece was damaged. When the airline replaced my bag they sent black. I ordered a carry on size and gave my husband the black set and replaced my large blue piece. If my hardside luggage is damaged again I won't be replacing it with the same brand".
    Classification: real

    Example 4:
    Review: "Didn't realize this was homeopathic, but I thought it would be a nice addition to the homeopathic.I had to get a toothbrush and comb out of the box, and now it's a little smaller.I think it's going to be a great addition to the home"
    Classification: fake

    Now classify this review:
    Review: "{text}"
    Classify this review as either "real" or "fake" (respond with only one word):"""