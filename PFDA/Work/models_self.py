def model_scorer(X_train,X_test,y_train,y_test):
    knn = KNeighborsRegressor(n_neighbors=3).fit(X_train, y_train)
    train_score_knn = knn.score(X_train, y_train)
    test_score_knn = knn.score(X_test, y_test)

    lr = LinearRegression().fit(X_train, y_train)
    train_score_lr = lr.score(X_train, y_train)
    test_score_lr = lr.score(X_test, y_test)

    # nsvr = NuSVR(nu=.8, C=.4).fit(X_train, y_train)
    # train_score_nsvr = nsvr.score(X_train, y_train)
    # test_score_nsvr = nsvr.score(X_test, y_test)

    ard = ARDRegression(normalize=True, alpha_1= 5e-1 , alpha_2= 5e-1,lambda_1= 1e-1, lambda_2= 1e-1 ).fit(X_train, y_train)
    train_score_ard = ard.score(X_train, y_train)
    test_score_ard = ard.score(X_test, y_test)

    score_train = [train_score_nsvr, train_score_ard, train_score_bagr, train_score_gbr]
    score_test = [test_score_nsvr, test_score_ard, test_score_bagr, test_score_gbr]
    model = ['knn', 'lr', 'ard']

    score_dict = {
    'train_score':score_train,
    'test_score':score_test
    }

    df_score = pd.DataFrame(score_dict, index = model)
    return df_score