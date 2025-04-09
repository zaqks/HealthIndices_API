from math import pi, sqrt


def get_calibration():
    try:
        with open('calibration.txt', 'r') as f:
            return float(f.read().strip())
    except:
        return None


model = None
# from model_app.ai.U2Net_BodyMeasurement.U2Net_BodyMeasurement import BodyMeasurer
# from ui_app.models import Score
# model = BodyMeasurer(resize_factor=get_calibration(),  out_dir='db')

# print("-"*30)
# print(f'calibration: {model.resize_factor}')
# print("-"*30)


def calc_bri(ws, hs):
    print("-"*30)
    print(ws, hs)
    print("-"*30)

    # P
    a, b = ws
    a /= 2
    b /= 2

    p = 2*pi*sqrt((a**2 + b**2)/2)
    # H
    h = sum(hs)/2

    #
    rslt = 364.3 - 365.5 * sqrt(1-(p/(3.14*h))**2)
    # SAVE TO THE DB
    Score(bri=rslt, height=h, waist=p).save()
    #
    return p, h, rslt
