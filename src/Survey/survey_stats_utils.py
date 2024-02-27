"""
Some statistics from the all_questionnaire_df
"""

# ====================================================================================================================
# Imports
# ====================================================================================================================


from constants import pd

#TODO Fix All Below 

# ====================================================================================================================
# Gender, Age, Grade, Major, Risk
# ====================================================================================================================


def gen_gender_dict(all_questionnaire_df: pd.DataFrame):
    """
    Gender breakdown

    :param all_questionnaire_df: conbined DF from our 3 survey types
    :return gender_dict: information regarding gender
    """
    # Count the occurrences of each unique value in the 'Fruit' column
    count_gender_series = all_questionnaire_df['player.gender'].value_counts()

    gender_dict = count_gender_series.to_dict

    gender_dict_structure = {1.0: 0,
                             2.0: 0,
                             3.0: 0
                             }

    # Convert the Series to a dictionary
    gender_dict_final = {key: gender_dict.get(key, 0) + gender_dict_structure.get(key, 0) for key in set(gender_dict) | set(gender_dict_structure)}
    gender_dict = count_gender_series.to_dict()

    gender_dict_final['female'] =  gender_dict.pop(2.0)
    gender_dict_final['male'] =  gender_dict.pop(1.0)
    gender_dict_final['other'] =  gender_dict.pop(3.0)

    return gender_dict_final




def gen_grade_dict(all_questionnaire_df: pd.DataFrame):
    """
    Grade breakdown

    :param all_questionnaire_df: conbined DF from our 3 survey types
    """
    count_grade_series = all_questionnaire_df['player.grade'].value_counts()

    grade_dict = count_grade_series.to_dict()

    grade_dict['freshman'] =  grade_dict.pop(1.0)
    grade_dict['sophomore'] =  grade_dict.pop(2.0)
    grade_dict['junior'] =  grade_dict.pop(3.0)
    grade_dict['senior'] =  grade_dict.pop(4.0)
    grade_dict['graduate'] =  grade_dict.pop(5.0)

    return grade_dict

# TODO we use levels for major
def gen_major_dict(all_questionnaire_df: pd.DataFrame):
    """
    Major breakdown

    :param all_questionnaire_df: conbined DF from our 3 survey types
    """
    count_major_series = all_questionnaire_df['player.major'].value_counts()

    major_dict = count_major_series.to_dict()

    return major_dict



# ====================================================================================================================
# 5-Point Scale Questions 
# ====================================================================================================================

def gen_motivation_dict(all_questionnaire_df: pd.DataFrame, column_name: str):
    """
    The breakdowns for all questions regarding the format of what motivated your response, since they use the same scaling,
    can be generated with this function

    :param all_questionnaire_df: conbined DF from our 3 survey types
    :return: dict breakdown of the reason why x investment from subjects on a scale
    """
    count_motivation_series = all_questionnaire_df[column_name].value_counts()

    moviation_dict = count_motivation_series.to_dict()

    motivation_structure = {1.0: 0,
                           2.0: 0,
                           3.0: 0,
                           4.0: 0,
                           5.0: 0
                           }

    motivation_dict_final = {key: moviation_dict.get(key, 0) + motivation_structure.get(key, 0) for key in set(moviation_dict) | set(motivation_structure)}

    motivation_dict_final['strongly agree'] = motivation_dict_final.pop(1.0)
    motivation_dict_final['agree'] = motivation_dict_final.pop(2.0)
    motivation_dict_final['disagree'] = motivation_dict_final.pop(3.0)
    motivation_dict_final['strongly disagree'] = motivation_dict_final.pop(4.0)
    motivation_dict_final['uncertain'] = motivation_dict_final.pop(5.0)

    return motivation_dict_final


# ====================================================================================================================
# Decision Style #TODO Make 4 level version
# ====================================================================================================================

def gen_decision_style_aaron_dict(all_questionnaire_df: pd.DataFrame):
    """
    Initial Survey had 5 levels for this style of question so those resposnes are stored separately in this function
    Relevent session code: v90x8oti

    :param all_questionnaire_df: conbined DF from our 3 survey types
    :return: facts_dict_final, feelings_dict_final
    """
    questionnaire_aaron_df = all_questionnaire_df[all_questionnaire_df['session.code']=='v90x8oti']

    # Decision Style Facts
    count_facts_series = questionnaire_aaron_df['player.decision_style_facts'].value_counts()
    facts_dict = count_facts_series.to_dict()

    decition_style_aaron_structure = {1.0: 0,
                                      2.0: 0,
                                      3.0: 0,
                                      4.0: 0,
                                      5.0: 0}
    
    facts_dict_final = {key: facts_dict.get(key, 0) + decition_style_aaron_structure.get(key, 0) for key in set(facts_dict) | set(decition_style_aaron_structure)}

    facts_dict_final['always'] = facts_dict_final.pop(1.0)
    facts_dict_final['usually'] = facts_dict_final.pop(2.0)
    facts_dict_final['sometimes'] = facts_dict_final.pop(3.0)
    facts_dict_final['rarely'] = facts_dict_final.pop(4.0)
    facts_dict_final['never'] = facts_dict_final.pop(5.0)

    # Decision Style Feelings
    count_feelings_series = questionnaire_aaron_df['player.decision_style_feelings'].value_counts()
    feelings_dict = count_feelings_series.to_dict()

    feelings_dict_final = {key: feelings_dict.get(key, 0) + decition_style_aaron_structure.get(key, 0) for key in set(feelings_dict) | set(decition_style_aaron_structure)}

    feelings_dict_final['always'] = feelings_dict_final.pop(1.0)
    feelings_dict_final['usually'] = feelings_dict_final.pop(2.0)
    feelings_dict_final['sometimes'] = feelings_dict_final.pop(3.0)
    feelings_dict_final['rarely'] = feelings_dict_final.pop(4.0)
    feelings_dict_final['never'] = feelings_dict_final.pop(5.0)

    return facts_dict_final, feelings_dict_final


# ====================================================================================================================
# Clarity
# ====================================================================================================================

def gen_clarity_dict(all_questionnaire_df: pd.DataFrame):
    """
    Instruction clarity scores

    :param all_questionnaire_df: conbined DF from our 3 survey types
    """
    count_clarity_series = all_questionnaire_df['player.clarity'].value_counts()

    clarity_dict = count_clarity_series.to_dict()

    clarity_dict_structure = {1.0: 0,
                           2.0: 0,
                           3.0: 0,
                           4.0: 0,
                           5.0: 0,
                           }

    clarity_dict_final = {key: clarity_dict.get(key, 0) + clarity_dict_structure.get(key, 0) for key in set(clarity_dict) | set(clarity_dict_structure)}

    clarity_dict_final['strongly disagree'] = clarity_dict_final.pop(5.0)
    clarity_dict_final['disagree'] = clarity_dict_final.pop(4.0)
    clarity_dict_final['agree'] = clarity_dict_final.pop(2.0)
    clarity_dict_final['strongly agree'] = clarity_dict_final.pop(1.0)
    clarity_dict_final['dont know'] = clarity_dict_final.pop(5.0)

    return clarity_dict_final


# ====================================================================================================================
# TODO Summary statistics where relevant on particular survey questions
# ====================================================================================================================


# ====================================================================================================================
# TODO Text analysis (NLP) on short answer Qs 
# ====================================================================================================================
