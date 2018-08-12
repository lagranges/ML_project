from feature_engineering.T_fe_combined_from_different_tables import get_features_1_1
from models.cv_lightGBM import *

import global_vars

# Setting

global_vars.prefix = "T_experimentation_1"
log_dir = "../../logs/"
submissions_dir = "../../submissions/"

# logging
level = global_vars.logging.INFO
level = global_vars.logging.INFO
format = '  %(message)s'
handlers = [global_vars.logging.FileHandler(log_dir + global_vars.prefix + '.log'), global_vars.logging.StreamHandler()]
global_vars.logging.basicConfig(level = level, format = format, handlers = handlers)


# Feature Engineering

df = get_features_1_1(debug=False)

# Modeling
# Try to write the result such as images, log files, feature importance.txt at this step

test_df = kfold_lightgbm(df, num_folds=5, stratified=False, debug=True)

# Submission

test_df.to_csv(submissions_dir + global_vars.prefix + ".csv", index=False)

