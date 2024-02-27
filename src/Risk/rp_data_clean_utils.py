"""
Data cleaning and reading code for the risk preference data
"""


# ====================================================================================================================
# Imports
# ====================================================================================================================


from constants import pd


# ====================================================================================================================
# Data Reading and Cleaning
# ====================================================================================================================


def rp_reading_and_cleaning(filename: str):
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
  # rename columns that could become problematic when I combine the entire dataframe
  dataframe.rename(columns={
    'player.id_in_group':'player.id_in_group_lottery',
    'player.payoff':'player.payoff_lottery',
    'player.start_time':'player.start_time_lottery',
    'player.time_spent_results':'player.time_spent_results_lottery',
    'group.id_in_subsession':'group.id_in_subsession_lottery',
    'subsession.round_number':'subsession.round_number_lottery'
    }, inplace=True)

  return dataframe