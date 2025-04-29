import win32com.client as win32

# Signature for CineMarga marketing emails
signature = '''
<br>
<div>
    <b><span style='font-size:12.0pt;font-family:"Arial",sans-serif;color:gray;'>CineMarga</span></b>
    <br>
    <b><span style='padding:0px;font-size:10.0pt;font-family:"Arial",sans-serif;color:gray;'>Explore. Rate. Celebrate Nepali Cinema.</span></b>
    <br>
    <span style='font-size:10.0pt;font-family:"Arial",sans-serif;color:gray;'>
        <a href="https://cinemarga.com" target="_blank"><span style='font-size:10.0pt;font-family:"Arial",sans-serif;color:blue'>https://cinemarga.com</span></a>
    </span>
    <br>
    <span style='font-size:10.0pt;font-family:"Arial",sans-serif;color:gray;'>E-mail: </span>
    <span style='color:gray;'>
        <a href="mailto:contact@cinemarga.com" target="_blank"><span style='font-size:10.0pt;font-family:"Arial",sans-serif;color:blue'>contact@cinemarga.com</span></a>
    </span>
    <br>
</div>
'''

# Table template with CineMarga links
table_template = '''
<table cellspacing="0" cellpadding="2" style="text-align:center;border:1px solid black; border-collapse: collapse; font-family: Calibri; font-size:11pt; vertical-align:top">
    <tr style="border:1px solid black; vertical-align:top; padding:10px">
        <td colspan="4" bgcolor="darkred" style="color:white;border:1px solid black; font-weight: bold; font-size:1.2em">
            CineMarga <a href="{site_url}" style="color:white;">{site_url}</a>
        </td>
    </tr>
    <tr style="border:1px solid black; vertical-align:top; padding:7px">        
        <td bgcolor="darkred" width="100" style="color:white;border:1px solid black; font-weight: bold;">Social</td>
        <td bgcolor="darkred" width="150" style="color:white;border:1px solid black; font-weight: bold;">Community</td>
        <td bgcolor="darkred" width="130" style="color:white;border:1px solid black; font-weight: bold;">Articles</td>
        <td bgcolor="darkred" width="100" style="color:white;border:1px solid black; font-weight: bold;">Reviews</td>            
    </tr>
    <tr style="border:1px solid black; vertical-align:top; padding:7px">
        <td style="border:1px solid black; font-style: italic; "><a href="{fb_url}">Facebook</a></td>
        <td style="border:1px solid black; font-style: italic; "><a href="{reddit_url}">Reddit</a></td>
        <td style="border:1px solid black; font-style: italic; "><a href="{blog_url}">Cine Blog</a></td>
        <td style="border:1px solid black; font-style: italic; "><a href="{yt_url}">YouTube</a></td>
    </tr>
    <tr style="border:1px solid black; vertical-align:top; padding:7px">
        <td style="border:1px solid black; font-style: italic;"><a href="{ig_url}">Instagram</a></td>
        <td style="border:1px solid black; font-style: italic;"></td>
        <td style="border:1px solid black; font-style: italic;"></td>
        <td style="border:1px solid black; font-style: italic;"></td>
    </tr>
</table>
'''

# Send or display email based on auto flag


def manage_display_auto_send(mail, auto=False):
    if auto:
        print("sending email...")
        mail.Send()
        print("email sent 😎")
    else:
        print("opening the email in outlook, check the program")
        mail.Display(True)  # open in outlook

# Build basic email structure


def build_basic_email(subject, to_list, cc_list):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to_list
    mail.CC = cc_list
    mail.Subject = subject
    return mail

# Build CineMarga marketing email


def build_email_CineMarga(to, cc, auto=False):
    # Default values for 'to' and 'cc'
    if to == "":
        to = "nishakirangnawaly@gmail.com"
    elif to == 'e':  # leave field empty
        to = ""

    if cc == "":
        cc = "11pksuman@gmail.com"
    elif cc == 'e':  # leave field empty
        cc = ""

    # Prompt for subject or default to 'New mission'
    default_subject = 'New mission'
    subject = input(f"Subject (blank for default '{default_subject}'): ")
    if subject == "":
        subject = default_subject

    # Create mail object
    mail = build_basic_email(subject, to, cc)

    # Build the email body with a signature and table links
    # Build the email body with a new format and signature
    body = (f"<span style='font-family: Calibri; font-size:11pt;'>"
            f"Subject: Cinemarga: A Platform to Celebrate Nepali Cinema – Seeking Collaboration with Nepal Movie Board<br><br>"

            f"Dear [Recipient's Name],<br><br>"

            f"I hope this email finds you well. My name is Nisha Kiran Gnawaly, and I am the co-founder and front-end designer of Cinemarga, "
            f"a platform dedicated to exploring, celebrating, and promoting Nepali cinema. We are committed to providing a space where Nepali films "
            f"can be discovered, rated, and discussed by movie lovers across the globe.<br><br>"

            f"Our platform allows users to:<br><br>"
            f"• Discover Nepali films through a comprehensive movie database<br>"
            f"• Rate and review films, contributing to a growing, community-driven database<br>"
            f"• Track movies on personalized watchlists<br>"
            f"• Stay connected with the vibrant Nepali film industry<br><br>"

            f"At Cinemarga, we believe in the power of data and community. To ensure we provide accurate and up-to-date information, "
            f"we would like to collaborate with the Nepal Movie Board and gain access to reliable data, film libraries, and resources "
            f"that will help enhance the user experience and ensure the quality of our content.<br><br>"

            f"As part of this initiative, we are reaching out to discuss the potential for collaboration, as well as how we can contribute "
            f"to the visibility and promotion of Nepali cinema through our platform.<br><br>"

            f"<strong>Key Benefits of Collaborating with Cinemarga:</strong><br><br>"
            f"• Access to a growing, engaged audience of Nepali film enthusiasts<br>"
            f"• Support in promoting Nepali films globally<br>"
            f"• Opportunities for data sharing and the integration of official film collections into our platform<br><br>"

            f"We would appreciate the opportunity to discuss this in more detail and explore potential partnership opportunities with the Nepal Movie Board.<br><br>"

            f"Please feel free to reach out to me directly at <a href='mailto:gnalwynishakiran@gmail.com'>gnalwynishakiran@gmail.com</a> "
            f"if you are interested in learning more or scheduling a meeting.<br><br>"

            f"Thank you for considering this opportunity, and we look forward to the possibility of working together.<br><br>"

            f"Best regards,<br><br>"
            f"Nisha Kiran Gnawaly<br>"
            f"Co-founder & Front-End Designer, Cinemarga<br>"
            f"<a href='mailto:gnalwynishakiran@gmail.com'>gnalwynishakiran@gmail.com</a><br>"
            f"<a href='https://www.cinemarga.com'>www.cinemarga.com</a><br><br>"
            f"</span>")

    # Attach HTML body and signature
    mail.HtmlBody = body + signature

    # Fill in the table template with CineMarga URLs
    body += table_template.format(
        site_url='https://cinemarga.com',
        fb_url='https://www.facebook.com/cinemarga',
        ig_url='https://www.instagram.com/cinemarga',
        reddit_url='https://www.reddit.com/r/CineMarga',
        yt_url='https://www.youtube.com/cinemarga',
        blog_url='https://cinemarga.com/blog'
    )
    body += "<br><br>Best regards,<br><br>CineMarga Team</span><br><br>"

    # Attach HTML body and signature
    mail.HtmlBody = body + signature

    # Send or display email
    manage_display_auto_send(mail, auto)

# Build a test email


def build_email_test(to, cc, auto=False):
    subject = input("Subject: ")
    mail = build_basic_email(subject, to, cc)
    mail.HtmlBody = "test build mail programmatically"
    manage_display_auto_send(mail, auto)

# Get email addresses from user


def getEmailAddresses(type_of_email="TO"):
    emails = input(
        f"{type_of_email} (blank to use default addresses or 'e' to leave field empty): ")

    if emails != "" and emails != 'e':
        # more than one email address must be separated by ;
        emails_splitted = emails.split("@")
        while len(emails_splitted) > 2 and emails.count(';') < int(len(emails_splitted)/2):
            print("use ; to separate addresses")
            emails = input(
                f"{type_of_email} (blank to use default addresses or 'e' to leave field empty): ")
            if emails == "" or emails == 'e':
                break

    return emails

# Email type dispatcher


def email_type_disptacher(email_type):
    to = getEmailAddresses("TO")
    cc = getEmailAddresses("cc")
    auto_send = input("automatic sending? [y/n] (default no): ")
    send = True if auto_send == "y" else False

    match email_type:
        case 1:
            build_email_CineMarga(to, cc, send)
        case 2:
            build_email_test(to, cc, send)

        # In case there is no match
        case _:
            return -1


# Main function to start email creation
if __name__ == "__main__":
    email_type = input("Choose what kind of email to build:\n"
                       "  1. CineMarga\n"
                       "  2. test\n"
                       "> ")

    email_type_disptacher(int(email_type))
