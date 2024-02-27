"""
Data cleaning and reading code for treatment data (baseline, additive random, and additive ambiguous)
"""


# ====================================================================================================================
# Imports
# ====================================================================================================================


from constants import pd


# ====================================================================================================================
# Data Reading and Cleaning
# ====================================================================================================================


def reading_and_cleaning(filename: str):
  """
  reads a csv file and removes any demo data from the file and drops columns 
  that are irrelevant to our analysis

  :param filename: the csv filename with relevant pathing information
  :return: a np.ndarray with rows and columns containing data from the strategy
  method portion of this experiment
  """
  # Read the data 
  dataframe = pd.read_csv(filename)
  # drop all rows that are demo (not usable data for ANY subsequent analysis)
  dataframe = dataframe[~(dataframe['session.is_demo'] == 1)]
  # Drop some sessions that were not compeleted
  values_to_remove = ['oneb7wj3', 'keyo9hp7', 'lcklukap']
  dataframe = dataframe[~dataframe['session.code'].isin(values_to_remove)]
  # drop columns that provide no information and are clutter
  dataframe.drop(['participant.label','participant._is_bot',
           'participant._index_in_pages','participant._max_page_index',
           'participant._current_app_name','participant._current_page_name',
           'participant.time_started_utc','participant.visited',
           'participant.mturk_worker_id','participant.mturk_assignment_id',
           'player.role', 'session.label', 'session.mturk_HITId',
           'session.mturk_HITGroupId', 'session.comment'],
          axis = 1, inplace = True)
  dataframe = dataframe.reset_index(drop=True)
  return dataframe


# ====================================================================================================================
# Merge Treatment DF with corresponding instructions data
# ====================================================================================================================


def merge_game_and_instrucs(treatment_df: pd.DataFrame, instrucs_df: pd.DataFrame, Treatment: str):
  """
    Append the instrucs dataframe to the relevent treatment dataframe

    :param treatment_df: treatment app dataframe
    :param instrucs_df: treatment instructions dataframe
    :return treatment_and_instrucs_df: merged df with relevent columns renamed
    """
  # Rename potentially problematic column names before merge 
  instrucs_df.rename(columns={
    'player.start_time': 'player.start_time_instrucs'
  }, inplace=True)

  game_and_instrucs_df = pd.merge(treatment_df, instrucs_df[['participant.code', 'player.comprehension_question_one', 'player.comprehension_question_two',
                                                             'player.comprehension_question_three_a', 'player.comprehension_question_three_b',
                                                             'player.comprehension_question_four_a', 'player.comprehension_question_four_b',
                                                             'player.comprehension_question_four_c', 'player.time_to_answer',
                                                             'player.start_time_instrucs', 'player.time_spent_instrucs', 'player.time_spent_compqs',
                                                             'player.num_errors_q_one', 'player.num_errors_q_two', 'player.num_errors_q_three_a',
                                                             'player.num_errors_q_three_b', 'player.num_errors_q_four_a', 'player.num_errors_q_four_b',
                                                             'player.num_errors_q_four_c']],
                                                             on='participant.code')
  
  game_and_instrucs_df['Treatment'] = Treatment

  game_and_instrucs_df.rename(columns ={
    'player.payoff': 'player.payoff_treatment',
    'player.start_time': 'player.start_time_treatment',
      'player.time_spent_results': 'player.time_spent_results_treatment'  
      })
  return game_and_instrucs_df


# ====================================================================================================================
# Combine the three treatment dfs into a mega df of the treatment data
# ====================================================================================================================


def gen_treatment_all_df(baseline_df: pd.DataFrame, random_df: pd.DataFrame, ambiguous_df: pd.DataFrame):
   """
   Make the megaladon data frame from all treatments

   :param baseline_df: Instrucs and app data set for the baseline pgg
   :param random_df: instruc and app data set for the additive-random pgg
   :param ambiguous_df: instruc and app data set for the additive-ambiguous pgg
   :return all_treatment_df: the mega dataframe for all treatment related apps 
   """
   all_treatment_df = pd.concat([baseline_df, random_df, ambiguous_df], axis=0, keys = ['baseline','random','additive'])
   return all_treatment_df
