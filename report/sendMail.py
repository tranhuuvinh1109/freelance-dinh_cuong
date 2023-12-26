from django.core.mail import send_mail
def send_mail_to_admin(location, recipient_list, report_date ):
    print("Sending mail to admin")
    subject = f"{location} - Báo cáo ngày {report_date}" 
    message = f"{location} đã tạo báo cáo thành công cho ngày {report_date}"
    send_mail(subject, message, 'vinhhuutran.developer@gmail.com', recipient_list)
    print("--------------")