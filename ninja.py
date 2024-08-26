import streamlit as st
import json
import os
import gspread
from datetime import datetime
import pytz

# 環境変数からサービスアカウントのJSON情報を読み込む
gcp_service_account_info = json.loads(os.environ['GCP_SERVICE_ACCOUNT_JSON'])

# gspreadに認証情報を渡してクライアントを初期化
gc = gspread.service_account_from_dict(gcp_service_account_info)

# titleの表示
st.title('Discover Japan with Expert Guide?')

st.header('About Soraie Ninja guide Service by Miley')
st.text("Asakusa guided tour")

# 画像の表示
kimono_image = st.image("z1.png", caption="Ninja Tour by a former idol Miley")
kimono_image = st.image("z2.png", caption="Temple, Karaoke, Food, etc.")

# 動画の表示
st.header('Introduction of Your guide Miley')

# サムネイル画像を表示
st.image("thumbnail.jpg", caption="Click below to play video (Watch out for sounds)", use_column_width=True)

# ユーザーがクリックしたら動画を表示する
if st.button("Play Video"):
    st.video("mileyintro.mp4", format="video/mp4")


st.subheader('Other outfits and other locations')
st.text("We also offer tours to Shinjuku/Akihabara etc.")

# sample schedule 画像の表示
kimono_image = st.image("schedule.jpg", caption="We can tailor it to meet your needs")


# 画像の表示
kimono_image = st.image("z3.png", caption="Other Tour Image")

# レビュー動画の表示
st.header('Reviews')
kimono_video = st.video("https://youtu.be/BoHJpedovFM")


st.header('Q&A')

# 価格、人数について
with st.expander("About Price"):
    st.markdown("""
    - **Are the prices shown on the website per person?**
        - Yes, it is 25,000 yen per person.
    - **How many people should be in the group to conduct a tour?**
        - The minimum number of participants is 2 people, and the maximum is 5 people.
    """)

# プライベートツアーについて
with st.expander("About Private Tours"):
    st.markdown("""
    - **Do you provide private tours?**
        - Yes, we provide private tours. The conditions for private tours are:
          - 2 people or more
          - At least 2 hours
          - Bar hopping is not allowed
          If you would like a private tour, please inquire through our private tour form.
    - **Do you provide custom tours?**
        - Private tours allow you to customize your tour. However, we may not be able to meet all your wishes. Please check the participation conditions for private tours before making a reservation.
    """)

# ツアーについて
with st.expander("Service"):
    st.markdown("""
    - **What time does the tour start?**
        - It depends on the tour. Please check the tour itinerary on the tour page. You can also check the confirmation email after making your reservation.
    - **Where is the meeting point?**
        - It depends on the tour. The meeting point for your tour is listed on each tour's page. You can also check the confirmation email after making your reservation.
    - **I am traveling alone. Can I join any tour?**
        - Solo travelers are very welcome to join our tours! We have many solo travelers on our tours.
    - **We are a big group (over 6 people). Can we book a tour?**
        - Yes, booking is possible. Please book through our private tour form.
    """)

# 予約について
with st.expander("About Reservations"):
    st.markdown("""
    - **How can I check my reservation?**
        - After booking, a confirmation email with your name, booking date, time, and meeting place will be sent to your email address. If you haven't received it yet, please contact us via our contact form.
    - **Can I add more people to my reservation?**
        - If the date is still available on the website, please book online. If the date is closed, please contact us through our contact form. We'll check availability and get back to you.
    - **I am traveling alone. Can I join any tour?**
        - Solo travelers are very welcome to join our tours! We have many solo travelers on our tours.
    """)

# お子様連れについて
with st.expander("About Children"):
    st.markdown("""
    - **Can I bring children to the tours?**
        - Children under 6 years old are not allowed on group tours. Small children (under 6 years old) are welcome on private tours. However, at least two participants aged 13 or older are required. Children under 12 years old are not counted toward the total number of guests as they are free of charge.
    - **Do you have a kids' price?**
        - Group tours are open to guests aged 6 and older, and we do not offer a kids' price. Private tours are free for children 12 and under. However, at least two participants aged 13 or older are required.
    """)

# 参加にあたって
with st.expander("Joining the Tour"):
    st.markdown("""
    - **Do I need to print out a voucher to join the tour?**
        - No, you don't need to print anything. Simply inform the guide of your name when you join the tour.
    - **Do you offer hotel pickup/drop-off service?**
        - We’re sorry, but we do not currently offer pickup or drop-off services.
    - **Do you offer tours in languages other than English?**
        - We can provide guides in Japanese if requested. Unfortunately, other languages are not currently supported.
    - **Can I pay the guide in cash on the day of the tour?**
        - Yes, cash payment is possible on the day of the tour.
    """)

# キャンセルと返金について
with st.expander("Cancellations and Refunds"):
    st.markdown("""
    - **When can I get a full refund?**
        - You can get a full refund if you cancel your booking at least 24 hours before the tour's starting time. You will also receive a refund if we are unable to provide the tour due to unavoidable circumstances or if the tour is canceled due to inclement weather.
    - **I think I have paid, but I didn't receive a confirmation email.**
        - The payment may not have gone through, and your tour might not be booked. Please return to the booking page and try again. If the payment has been processed, the email address might have been entered incorrectly. In this case, please contact us through our contact form, and we'll resolve the issue as soon as possible.
    - **Is there a cancellation fee?**
        - If you cancel at least 24 hours before the tour's starting time, there is no cancellation fee. However, if you cancel within 24 hours of the tour's starting time or after it has started, we will not be able to provide a refund.
    """)


# 予約フォーム
with st.form('Reservation Form'):
    st.header('Reservation Form')
    name = st.text_input('Name')
    address = st.text_input('Address')
    phone = st.text_input('Phone')
    email = st.text_input('Email')
    people_count = st.number_input('How many people', min_value=1)
    reservation_date = st.date_input('Reservation Date')
    
    # 予約時間の選択
    st.subheader('Reservation Time')
    reservation_time = st.selectbox('Select reservation time', options=[
        '9:00', '9:30', '10:00', '10:30',
        '11:00', '11:30', '12:00', '12:30',
        '13:00', '13:30', '14:00', '14:30',
        '15:00', '15:30', '16:00', '16:30'
    ])
    
    # 入力値のバリデーション
    all_fields_filled = name and address and phone and email
    today = datetime.now().date()
    valid_date = reservation_date >= today
    
    submitted = st.form_submit_button('SUBMIT')
    
    if submitted:
        if not all_fields_filled or not valid_date:
            if not all_fields_filled:
                st.error('Please fill in all the fields.')
            if not valid_date:
                st.error('Reservation Date must be today or later.')
        else:
            # 予約情報をスプレッドシートに記録
            # 以下のコードは、実際のGoogle Sheets APIの使用例です
            # 実際のアプリケーションでは、Google Sheets APIを設定し、認証を行う必要があります
            sh = gc.open("soraieninja")
            worksheet = sh.sheet1
            worksheet.append_row([
                name, address, phone, email, str(people_count), 
                str(reservation_date), reservation_time
            ])
            st.success('NOT DONE YET! Please Pay below to Reserve your spot. Your spots will not be confirmed until payment is made.')
            
            # 送信後に表示されるリンク(https://buy.stripe.com/7sIeWWbmA0oy6SQfZd)
            st.markdown('Please [CLICK HERE](https://buy.stripe.com/7sIeWWbmA0oy6SQfZd) to make a payment. (Our staff will contact you after your payment.)')