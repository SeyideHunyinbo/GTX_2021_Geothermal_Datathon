# GTX_2021_Geothermal_Datathon
Develop Machine Learning (ML) models to provide the prediction for the bottomhole predictions

This is a project based on the 2021 GTX Datathon (https://www.speuntapped.com)

# Problem Statement
The formation temperature is an important and decisive parameter in evaluation of geothermal potential. Despite the abundance of techniques for collecting drilling and well operation data, they do not necessarily provide the real Bottom Hole Temperature (BHT). The flowrate capacity of a geothermal well another important item that should be considered when analyzing data for viability evaluation.

Some oil and gas wells may show potentials of being converted into geothermal energy sources, and these potentials geothermal are based on the evaluation of the true bottomhole temperatures at and flow rates. Machine learning techniques can be valuable tools in the process of the finding solutions for this problem.

The well data such as well logs, formation tops, production and drilling data are gathered for two basins; one in US and the other in Canada. The steps involved in solving the problem include the following:

* `Data Exploration`: Perform data wrangling anf exploratory data analysis

* `Feature Selection and Engineering`: Determine which attributes are suitable for developing accurate models. Are there new features that need to be derived from the existing one to improve our model performance?

* `Modeling`: Perform hyper-parameter tuning where necessary and use the wrangled datasets to develop the models for predicting true bottomhole temperatures.

* `Model Deployment` : Save the models, wrap APIs around it and deploy in a production environment

* `Provide insights and recommendation`: Based on the model prediction results, provide practical insights and recommendations for tacking the challenge of retrofitting Oil & Gas wells into geothermal energy sources. Back it up with assumptions made for developing the solutions.

# Variables
* `US Field` : Contain well IDs, true formation temperatures (from static well logs and from synthetic sources), bottomhole temperatures (measured during drilling), production data, drilling data, formation tops, well-logs, and well location data

* `Canada Field` : Contain well IDs, true formation temperatures (from static well logs and from synthetic sources), bottomhole temperatures (from DST), production data, drilling data (exluding mud-weight and time since circulation data), formation tops, well-logs, and well location data

* `US Field` Mud Weight Data : EB_MW

* `US Field` Formation Tops Data : EB_FT

* `US Field` Well Headers : EB_WH

* `US Field` Production Data : EB_PS

* `Canada Field` Formation Tops Data : DV_FT

* `Canada Field` Well Headers : DV_WH

* `Canada Field` Production Data : DV_PS


# Files
This repo contains 7 files namely:

* `data_wrangling.py` : Python file for data wrangling

* `modelling_main_duv_eag.py` : Python file fo model development

* `deploy_models_main.py` : Python file for model developing (scripting still ongoing)


* `regr_eag.pkl` : Linear model for US Field

* `regr_duv.pkl` : Linear model for Canada Field

* `xgb_tuned_eag.pkl` : Tuned XGBoost model for US Field

* `xgb_tuned_duv.pkl` : Tuned XGBoost model for Canada Field

NB : The datasets (i.e. csv and xlsx files) are not provided as they are proprietary




