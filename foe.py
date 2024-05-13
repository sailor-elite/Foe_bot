import time
import cv2
import numpy as np
import sys
import pygetwindow as gw
import pyautogui
import mouse

money_img = cv2.imread("../../PycharmProjects/Foe_bot/images/money.jpg", cv2.IMREAD_COLOR)

hammer_img = cv2.imread("../../PycharmProjects/Foe_bot/images/hammer.jpg", cv2.IMREAD_COLOR)
hammer_produce = cv2.imread("../../PycharmProjects/Foe_bot/images/production.jpg", cv2.IMREAD_COLOR)

soldier = cv2.imread("../../PycharmProjects/Foe_bot/images/soldier.jpg", cv2.IMREAD_COLOR)
training = cv2.imread("../../PycharmProjects/Foe_bot/images/train.jpg", cv2.IMREAD_COLOR)

pack = cv2.imread("../../PycharmProjects/Foe_bot/images/pack.jpg", cv2.IMREAD_COLOR)
pack_produce = cv2.imread("../../PycharmProjects/Foe_bot/images/pack_produce.jpg", cv2.IMREAD_COLOR)

x_button = cv2.imread("../../PycharmProjects/Foe_bot/images/x_button.jpg", cv2.IMREAD_COLOR)

star_button = cv2.imread("../../PycharmProjects/Foe_bot/images/star.jpg", cv2.IMREAD_COLOR)
support_button = cv2.imread("../../PycharmProjects/Foe_bot/images/support.jpg", cv2.IMREAD_COLOR)
redeem_button = cv2.imread("../../PycharmProjects/Foe_bot/images/redeem.jpg", cv2.IMREAD_COLOR)




def get_Picture_FOE():
    """
    Change when using other browser

    :return:
    """
    w = gw.getWindowsWithTitle('Forge of Empires - Google Chrome')[0]
    w.activate()
    money_bool = False
    hammer_bool = False
    soldier_bool = False
    pack_bool = False
    x_button_bool = False
    star_bool = False

    base_img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
    frame = np.array(base_img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result_money = cv2.matchTemplate(frame, money_img, cv2.TM_CCOEFF_NORMED)
    result_hammer = cv2.matchTemplate(frame, hammer_img, cv2.TM_CCOEFF_NORMED)
    result_soldier = cv2.matchTemplate(frame, soldier, cv2.TM_CCOEFF_NORMED)
    result_pack = cv2.matchTemplate(frame, pack, cv2.TM_CCOEFF_NORMED)
    result_x_button = cv2.matchTemplate(frame, x_button, cv2.TM_CCOEFF_NORMED)
    result_star_button = cv2.matchTemplate(frame, star_button, cv2.TM_CCOEFF_NORMED)

    w_money = money_img.shape[1]
    h_money = money_img.shape[0]
    x_money_coord = 0
    y_money_coord = 0

    w_hammer = hammer_img.shape[1]
    h_hammer = hammer_img.shape[0]
    x_hammer_coord = 0
    y_hammer_coord = 0

    w_soldier = soldier.shape[1]
    h_soldier = soldier.shape[0]
    x_soldier = 0
    y_soldier = 0

    w_pack = pack.shape[1]
    h_pack = pack.shape[0]
    x_pack = 0
    y_pack = 0

    w_star_button = star_button.shape[1]
    h_star_button = star_button.shape[1]
    x_star_button = 0
    y_star_button = 0

    threshold = .64

    threshold_x_button = .9

    threshold_star_button = 0.9

    ylocm, xlocm = np.where(result_money >= threshold)

    yloch, xloch = np.where(result_hammer >= threshold)

    ylocs, xlocs = np.where(result_soldier >= threshold)

    ylocp, xlocp = np.where(result_pack >= threshold)

    ylocsb, xlocsb = np.where(result_star_button >= threshold_star_button)

    rectangles_soldier = []
    rectangles_money = []
    rectangles_hammer = []
    rectangles_training = []
    rectangles_pack = []
    rectangles_pack_produce = []
    rectangles_hammer_produce = []
    rectangles_star_button = []
    rectangles_x_button = []
    rectangles_support_button = []
    rectangles_redeem_button = []

    if x_button_bool is False:
        for (x, y) in zip(xlocm, ylocm):
            rectangles_money.append([int(x), int(y), int(w_money), int(h_money)])
            rectangles_money.append([int(x), int(y), int(w_money), int(h_money)])

        for (x, y) in zip(xloch, yloch):
            rectangles_hammer.append([int(x), int(y), int(w_hammer), int(h_hammer)])
            rectangles_hammer.append([int(x), int(y), int(w_hammer), int(h_hammer)])

        for (x, y) in zip(xlocs, ylocs):
            rectangles_soldier.append([int(x), int(y), int(w_soldier), int(h_soldier)])
            rectangles_soldier.append([int(x), int(y), int(w_soldier), int(h_soldier)])

        for (x, y) in zip(xlocp, ylocp):
            rectangles_pack.append([int(x), int(y), int(w_pack), int(h_pack)])
            rectangles_pack.append([int(x), int(y), int(w_pack), int(h_pack)])

        for (x, y) in zip(xlocsb, ylocsb):
            rectangles_star_button.append([int(x), int(y), int(w_star_button), int(h_star_button)])
            rectangles_star_button.append([int(x), int(y), int(w_star_button), int(h_star_button)])

    rectangles_money, weights_money = cv2.groupRectangles(rectangles_money, 1, 0.2)

    rectangles_hammer, weights_hammer = cv2.groupRectangles(rectangles_hammer, 1, 0.2)

    rectangles_soldier, weights_soldier = cv2.groupRectangles(rectangles_soldier, 1, 0.2)

    rectangles_pack, weights_pack = cv2.groupRectangles(rectangles_pack, 1, 0.2)

    result_star_button, weights_star_button = cv2.groupRectangles(rectangles_star_button, 1, 0.2)

    if hammer_bool is False and money_bool is False and soldier_bool is False and pack_bool is False and star_bool is False:
        base_img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
        frame = np.array(base_img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        w_x_button = x_button.shape[1]
        h_x_button = x_button.shape[0]
        x_x_button_coord = 0
        y_x_button_coord = 0

        ylocxb, xlocxb = np.where(result_x_button >= threshold_x_button)
        if ylocxb and xlocxb is not None:
            x_button_bool = True
            for (xxb, yxb) in zip(xlocxb, ylocxb):
                rectangles_x_button.append([int(xxb), int(yxb), int(w_x_button), int(h_x_button)])
                rectangles_x_button.append([int(xxb), int(yxb), int(w_x_button), int(h_x_button)])

            rectangles_x_button, weights_x_button = cv2.groupRectangles(rectangles_x_button, 1, 0.2)

            for (xxb, yxb, w_x_button, h_x_button) in rectangles_x_button:

                mouse.move(xxb, yxb)
                time.sleep(0.2)
                mouse.click()
                time.sleep(0.2)
                break
            time.sleep(0.2)
            base_img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
            frame = np.array(base_img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            ylocxb = None
            xlocxb = None
        else:
            x_button_bool = False
        base_img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
        frame = np.array(base_img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if x_button_bool is False:
        for (x, y, w_pack, h_pack) in rectangles_pack:
            pack_bool = True
            time.sleep(0.2)
            mouse.move(x + (w_pack / 2), y + (h_pack / 2))
            time.sleep(0.2)
            mouse.click()
            time.sleep(2)
            mouse.click()
            time.sleep(0.5)

            base_img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
            frame = np.array(base_img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            w_pack_produce = pack_produce.shape[1]
            h_pack_produce = pack_produce.shape[0]
            x_pack_produce = 0
            y_pack_produce = 0

            result_pack_produce = cv2.matchTemplate(frame, pack_produce, cv2.TM_CCOEFF_NORMED)
            ylocpp, xlocpp = np.where(result_pack_produce >= threshold)

            for (xpp, ypp) in zip(xlocpp, ylocpp):
                rectangles_training.append([int(xpp), int(ypp), int(w_pack_produce), int(h_pack_produce)])
                rectangles_training.append([int(xpp), int(ypp), int(w_pack_produce), int(h_pack_produce)])

            for (xpp, ypp, w_pack_produce, h_pack_produce) in rectangles_pack_produce:
                mouse.move(xpp + (w_pack_produce / 2), ypp + (h_pack_produce / 2))
                time.sleep(0.4)
                mouse.click()
                time.sleep(0.4)
                break
            pack_bool = False

        for (x, y, w_soldier, h_soldier) in rectangles_soldier:
            soldier_bool = True
            time.sleep(0.2)
            mouse.move(x + (w_soldier / 2), y + (h_soldier / 2))
            time.sleep(0.2)
            mouse.click()
            time.sleep(2)
            mouse.click()
            time.sleep(0.5)

            base_img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
            frame = np.array(base_img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            w_training = training.shape[1]
            h_training = training.shape[0]
            x_training = 0
            y_training = 0

            result_train = cv2.matchTemplate(frame, training, cv2.TM_CCOEFF_NORMED)
            yloct, xloct = np.where(result_train >= threshold)
            for (xt, yt) in zip(xloct, yloct):
                rectangles_training.append([int(xt), int(yt), int(w_training), int(h_training)])
                rectangles_training.append([int(xt), int(yt), int(w_training), int(h_training)])
            for (xt, yt, w_training, h_training) in rectangles_training:
                mouse.move(xt + (w_training / 2), yt + (h_training / 2))
                time.sleep(0.4)
                mouse.click()
                time.sleep(0.4)
                soldier_bool = False
                break
        print(rectangles_money)
        for (x, y, w_money, h_money) in rectangles_money:
            money_bool = True

            mouse.move(x, y + (h_money / 2))
            time.sleep(0.2)
            mouse.click()
            base_img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
            frame = np.array(base_img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            w_x_button = x_button.shape[1]
            h_x_button = x_button.shape[0]
            x_x_button_coord = 0
            y_x_button_coord = 0

            ylocxb, xlocxb = np.where(result_x_button >= threshold_x_button)
            if ylocxb and xlocxb is not None:
                money_bool = False
                break

        for (x, y, w_hammer, h_hammer) in rectangles_hammer:
            hammer_bool = True

            mouse.move(x, y + (h_hammer / 2) + 14)
            mouse.click()
            time.sleep(2)
            mouse.click()
            time.sleep(0.5)

            base_img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
            frame = np.array(base_img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            w_hammer_produce = hammer_produce.shape[1]
            h_hammer_produce = hammer_produce.shape[0]
            x_hammer_produce = 0
            y_hammer_produce = 0

            result_hammer_produce = cv2.matchTemplate(frame, hammer_produce, cv2.TM_CCOEFF_NORMED)

            ylochp, xlochp = np.where(result_hammer_produce >= threshold)

            for (xhp, yhp) in zip(xlochp, ylochp):
                rectangles_hammer_produce.append([int(xhp), int(yhp), int(w_hammer_produce), int(h_hammer_produce)])
                rectangles_hammer_produce.append([int(xhp), int(yhp), int(w_hammer_produce), int(h_hammer_produce)])

            for (xhp, yhp, w_hammer_produce, h_hammer_produce) in rectangles_hammer_produce:
                mouse.move(xhp + (w_hammer_produce / 2), yhp + (h_hammer_produce / 2))
                time.sleep(0.4)
                mouse.click()
                time.sleep(0.4)
                hammer_bool = False
                break

        for (x, y, w_star_button, h_star_button) in rectangles_star_button:
            star_bool = True
            mouse.move(x, y)
            time.sleep(0.1)
            mouse.click()

            base_img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
            frame = np.array(base_img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            w_support_button = support_button.shape[1]
            h_support_button = support_button.shape[0]
            x_support_button = 0
            y_support_button = 0

            w_redeem_button = redeem_button.shape[1]
            h_redeem_button = redeem_button.shape[0]
            x_redeem_button = 0
            y_redeem_button = 0

            result_support_button = cv2.matchTemplate(frame, support_button, cv2.TM_CCOEFF_NORMED)
            result_redeem_button = cv2.matchTemplate(frame, redeem_button, cv2.TM_CCOEFF_NORMED)

            ylocsp, xlocsp = np.where(result_support_button >= threshold)
            ylocrb, xlocrb = np.where(result_redeem_button >= threshold)

            for (x_support_button, y_support_button) in zip(xlocsp, ylocsp):
                rectangles_support_button.append(
                    [int(x_support_button), int(y_support_button), int(w_support_button), int(h_support_button)])
                rectangles_support_button.append(
                    [int(x_support_button), int(y_support_button), int(w_support_button), int(h_support_button)])

            for (x_redeem_button, y_redeem_button) in zip(xlocrb, ylocrb):
                rectangles_redeem_button.append(
                    [int(x_redeem_button), int(y_redeem_button), int(w_redeem_button), int(h_redeem_button)])
                rectangles_redeem_button.append(
                    [int(x_redeem_button), int(y_redeem_button), int(w_redeem_button), int(h_redeem_button)])

            for (x_support_button, y_support_button, w_support_button, h_support_button) in rectangles_support_button:
                    mouse.move(x_support_button + (w_support_button / 2), y_support_button + (h_support_button / 2))
                    time.sleep(0.4)
                    mouse.click()
                    time.sleep(0.4)
                    rectangles_support_button =[]
                    break

            for (x_redeem_button, y_redeem_button, w_redeem_button, h_redeem_button) in rectangles_redeem_button:
                mouse.move(x_redeem_button + (w_redeem_button / 2), y_redeem_button + (h_redeem_button / 2))
                time.sleep(0.4)
                mouse.click()
                time.sleep(0.4)
                rectangles_redeem_button = []
                break
            star_bool = False
    print ("money",money_bool,hammer_bool,pack_bool,star_bool,x_button_bool,soldier_bool)

    '''
    cv2.imshow('base', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        sys.exit()
        #uncomment to see actual frames
    '''