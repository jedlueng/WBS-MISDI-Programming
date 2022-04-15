def model_scorer(X_train,X_test,y_train,y_test):
    bagr = BaggingRegressor(n_estimators=15, max_samples=.6,max_features= .6).fit(X_train, y_train)
    train_score_bagr = bagr.score(X_train, y_train)
    test_score_bagr = bagr.score(X_test, y_test)

    gbr = GradientBoostingRegressor(n_estimators=40 , learning_rate=.01, subsample=.7,max_depth = 3).fit(X_train, y_train)
    train_score_gbr = gbr.score(X_train, y_train)
    test_score_gbr = gbr.score(X_test, y_test)

    nsvr = NuSVR(nu=.8, C=.4).fit(X_train, y_train)
    train_score_nsvr = nsvr.score(X_train, y_train)
    test_score_nsvr = nsvr.score(X_test, y_test)

    ard = ARDRegression(normalize=True, alpha_1= 5e-1 , alpha_2= 5e-1,lambda_1= 1e-1, lambda_2= 1e-1 ).fit(X_train, y_train)
    train_score_ard = ard.score(X_train, y_train)
    test_score_ard = ard.score(X_test, y_test)

    score_train = [train_score_nsvr, train_score_ard, train_score_bagr, train_score_gbr]
    score_test = [test_score_nsvr, test_score_ard, test_score_bagr, test_score_gbr]
    model = ['nsvr', 'ard', 'bagr', 'gbr']

    score_dict = {
    'train_score':score_train,
    'test_score':score_test
    }

    df_score = pd.DataFrame(score_dict, index = model)
    return df_score