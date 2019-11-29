def bayesiano(nombre_c,correo_c,tocupacion_c,mayor_c,compras_c,pcomprados_c):
    #nombre_c = requests.get("nombre")
    #correo_c = requests.get("correo")
    #LAS VARIABLES QUE SE LEAN POR PANTALLA
    #nombre_c='Julio Pernett'
    #correo_c='jjpernett2008@gmail.com'
    #Datos que se le pasan a bayes
    #Dtocupacion_c=0
    #Dmayor_c=1
    #Dcompras_c=2
    #Dpcomprados_c=1

    import pandas as pd

    Datos = pd.read_csv('Datos_Balegria.csv')
    #Datos.head(7)
    features_train = Datos.iloc[0:7,0:4]
    target_train = Datos.iloc[0:7,4]

    #Import  LabelEncoder
    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    f0=le.fit_transform(features_train.iloc[0:7,0])
    f1=le.fit_transform(features_train.iloc[0:7,1])
    f2=le.fit_transform(features_train.iloc[0:7,2])
    f3=le.fit_transform(features_train.iloc[0:7,3])
    label=le.fit_transform(target_train)
    features=list(zip(f0,f1,f2,f3))
    #print(features)
    #print(label)

    from sklearn.naive_bayes import GaussianNB

    def bayes(Dato1,Dato2,Dato3,Dato4):
        model1 = GaussianNB()
        model1.fit(features,label)
        Predicted = model1.predict([[Dato1,Dato2,Dato3,Dato4]])
        return Predicted

    Prediccion=bayes(tocupacion_c,mayor_c,compras_c,pcomprados_c)

    #Cargando archivo de configuración para envio de el correo electronico
    import yaml
    yaml.warnings({'YAMLLoadWarning': False})
    with open('config.yml', 'r') as config_file:
        config = yaml.load(config_file)

    msg_sbj = 'Apreciado ' + nombre_c + ' bienvenido al Banco Alegria'

    #armamos el mensaje de acuerdo al resultado de la predicción
    if Prediccion[0]==0:
        msg_text = '''Hola apreciado cliente,
        esta información puede ser de tú interes.\n
        haz sido favorecido con una de nuestras tarjetas de crédito de HOGAR\n\n
        ¡Muchas gracias por tu atención!'''
    elif Prediccion[0]==1:
        msg_text = '''Hola apreciado cliente,
        esta información puede ser de tú interes.\n
        haz sido favorecido con una de nuestras tarjetas de crédito de SALUD\n\n
        ¡Muchas gracias por tu atención!'''    
    elif Prediccion[0]==2:
        msg_text = '''Hola apreciado cliente,
        esta información puede ser de tú interes.\n
        haz sido favorecido con una de nuestras tarjetas de crédito de VIAJES\n\n
        ¡Muchas gracias por tu atención!'''       

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    me = "Banco Alegria <crmprueba111@gmail.com>"
    you= nombre_c + '<' + correo_c + '>'
    msg = MIMEMultipart()
    msg['From'] = me
    msg['To'] = you
    msg['Subject'] = msg_sbj
    msg.attach(MIMEText(msg_text, 'plain'))

    #ENVIO DE CORREO
    import smtplib
    with smtplib.SMTP_SSL(config['EMAIL']['smtp_server'], config['EMAIL']['port']) as s:
        s.ehlo()
        s.login(config['EMAIL']['username'],config['EMAIL']['password'])
        s.sendmail(me, you, msg.as_string())
        s.quit()

    return ()