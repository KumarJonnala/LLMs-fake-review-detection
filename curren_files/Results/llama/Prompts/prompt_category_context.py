class Config:

    #file_path = "D:\OVGU _Saurabh\SEM 3\Review Project\Code\Datasets\sampled_deceptive_opinion_new.csv"

    model = "llama3.2:3b"

    # Define zero-shot classification prompt
    # text placeholder in the prompt template will be replaced with actual review text.
    zero_shot_prompt_template = """
    You are an expert at detecting fake and real reviews.

    Task: Classify the following review of a product that is listed on amazon as either "fake" or "real". Analyze the language and structure of the review,
	It should not be overly generic or templeted language,should not have sales-like wording.

    The products reviewed may belong to categories such as:
    Home and Kitchen, Sports and Outdoors, Electronics, Beauty, Clothing, Books, and similar retail categories.


    Review: "{text}"

    Classify this review as either "fake" or "real" (respond with only one word):"""

    # Define one-shot classification prompt with one example
    one_shot_prompt_template = """
     You are an expert at detecting fake and real reviews.

    Task: Classify the following review of a product that is listed on amazon as either "real" or "fake". Analyze the language and structure of the review,
	It should not be overly generic or templeted language,should not have sales-like wording and lacks details or specificity.

    The products reviewed may belong to categories such as:
    Home and Kitchen, Sports and Outdoors, Electronics, Beauty, Clothing, Books, and similar retail categories.

    Example:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Category : Watches
    Classification: fake

    Now classify this review:
    Review: "{text}"
    Classify this review as either "real" or "fake" (respond with only one word):"""

    # Define few-shot classification prompt with multiple examples
    few_shot_prompt_template = """
    You are an expert at detecting real and fake reviews.


    Task: Classify the following review of a product that is listed on amazon as either "real" or "fake". Analyze the language and structure of the review,
	It should not be overly generic or templeted language,should not have sales-like wording and lacks details or specificity.

    The products reviewed may belong to categories such as:
    Home and Kitchen, Sports and Outdoors, Electronics, Beauty, Clothing, Books, and similar retail categories.

    Here are some examples:

    Example 1:
    Review: "Great Watch. I have had this watch for a long time and it works great. I have one in my car and the other in my office. The watch itself is a great watch and is very easy to use. It is a perfect size for my wrist and is very easy to wear. I have used it with a portable watch and I can tell the watch is very well made. I have worn it with a watch band and it is very comfortable. I will buy another one for my phone. I would highly recommend this watch.Perfect for my kids. I love them.These are super lightweight and lightweight. I have used them for a couple of months and they are still working great. I would definitely recommend them to my son for those times when he is not going to be wearing a helmet.These work great. I have used them for about a month and they are still doing great.Works as advertised.This is my second pair of glasses, and I really like the quality of the material. The material is thin and very soft, and it's comfortable to wear. The material is also very easy to clean, and I haven't had a problem with the plastic being damaged. I also have the odd case on my older pair, which I got for my husband when I was a kid. The fact that it's made of a durable material is"
    Category : Watches
    Classification: fake
    Example 2:
    Review: "I received these in and decided to go ahead and test these for strength and if it will be a good workout. I love the medium to the very strongest. The lighter exercise band when stretched rolled up a few times on me and I would have to unroll and start again. I guess because I was pulling it out so hard. The others did fine. I could feel the tightness with those as I stretched it out. I may lay flat and try it on my ankles and legs next. I left out of town so I have not been able to test it that way. But I assure you, you will feel it in your arms. I would consider buying these for my neighbor who also wants to work her arm muscles, because I do not want to loan mine out, as I will continue to use the tighter bands.
    Category : Sports Fitness and outdoors
    Classification: real

    Now classify this review:
    Review: "{text}"
    Classify this review as either "real" or "fake" (respond with only one word):"""

