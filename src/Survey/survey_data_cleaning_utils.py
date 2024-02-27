"""
Data cleaning and reading code for Survey Data
"""

# ====================================================================================================================
# Imports
# ====================================================================================================================


from constants import pd


# ====================================================================================================================
# Data Reading and Cleaning
# ====================================================================================================================

def survey_reading_and_cleaning(filename: str):
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
# Concatenate the baseline with the additive survey
# ====================================================================================================================

def survey_concat_base_and_additive(base_survey_df: pd.DataFrame, additive_survey_df: pd.DataFrame):
  combined_survey_df = pd.concat([additive_survey_df, base_survey_df[['participant.code', 'player.password_to_start', 'player.major',
                                                                      'player.gender', 'player.grade', 'player.personal_versus_group',
                                                                      'player.change',
                                                                      'player.reason_own', 'player.reason_group', 'player.reason_conditional', 'player.reason_experiment',
                                                                      'player.reason_adjust', 'player.reason_future_rounds', 'player.decision_style_facts', 'player.decision_style_feelings',
                                                                      'player.decision_style_religious', 'player.decision_style_family', 'player.clarity', 'player.suggestions',
                                                                      'player.start_time', 'player.time_spent_survey_one', 'player.time_spent_survey_two',
                                                                      'player.time_spent_survey_three', 'player.time_spent_survey_four', 'session.code', 'participant.payoff']]],
                                                                      ignore_index=True)
  
  columns_to_drop = ['player.id_in_group', 'player.payoff', 'participant.id_in_session', 'subsession.round_number']
  combined_survey_df.drop(columns=columns_to_drop, inplace=True)
  return combined_survey_df

