class ConfigModel:

    model = "gemma3:12b"

    base_url = "http://localhost:11400"

    # Default dataset used for quick local runs.
    default_dataset_path = "Datasets/Amazon_Human_VS_ComputerFake.csv"

    dataset_paths = {
        "amazon_human_vs_computer": "Datasets/Amazon_Human_VS_ComputerFake.csv",
        "hotel_human_vs_humanfake": "Datasets/Hotel_Human_VS_HumanFake.csv",
        "hotel_human_vs_humanfake_relabelled": "Datasets/Hotel_Human_VS_HumanFake_relabelled.csv",
        "hotel_humanreal_vs_cg": "Datasets/Hotel_HumanReal_VS_CG.csv",
        "hotel_humanreal_vs_mixfake": "Datasets/Hotel_HumanReal_VS_MixFake.csv",
    }

    # Prompt source files under curren_files/Prompts.
    prompts_base_path = "curren_files/Prompts"
    prompt_file_paths = {
        "ver_1": "curren_files/Prompts/ver_1.py",
        "ver_2": "curren_files/Prompts/ver_2.py",
        "ver_3": "curren_files/Prompts/ver_3.py",
        "ver_4_hotel": "curren_files/Prompts/ver_4_hotelPrompt.py",
        "ver_5_amazon": "curren_files/Prompts/ver_5_amazonPrompt.py",
    }
    
    prompt_templates = {
        "ver_1": [
            "zero_shot_prompt_template",
            "one_shot_prompt_template",
            "few_shot_prompt_template",
        ],
        "ver_2": [
            "zero_shot_prompt_template",
            "one_shot_prompt_template",
            "few_shot_prompt_template",
        ],
        "ver_3": [
            "zero_shot_depth0_width0",
            "zero_shot_depth1_width1",
            "one_shot_depth0_width0",
            "one_shot_depth1_width1",
            "few_shot_depth0_width0",
            "few_shot_depth1_width1",
        ],
        "ver_4_hotel": [
            "zero_shot_prompt_template",
            "zero_shot_prompt_template2",
            "one_shot_prompt_template",
            "one_shot_prompt_template2",
            "few_shot_prompt_template",
            "few_shot_prompt_template2",
        ],
        "ver_5_amazon": [
            "zero_shot_prompt_template",
            "zero_shot_prompt_template2",
            "one_shot_prompt_template",
            "one_shot_prompt_template2",
            "few_shot_prompt_template",
            "few_shot_prompt_template2",
        ],
    }