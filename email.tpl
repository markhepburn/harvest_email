<%!
import datetime
today = datetime.date.today()
%>
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
  <meta charset="utf-8">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
  <!--[if mso]>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings xmlns:o="urn:schemas-microsoft-com:office:office">
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <style>
    td,th,div,p,a,h1,h2,h3,h4,h5,h6 {font-family: "Segoe UI", sans-serif; mso-line-height-rule: exactly;}
  </style>
  <![endif]-->
    <title>Weekly project budget summary</title>
    <style>
@media (max-width: 600px) {
  .sm-inline-block {
    display: inline-block !important;
  }
  .sm-h-32 {
    height: 32px !important;
  }
  .sm-w-full {
    width: 100% !important;
  }
  .sm-px-16 {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }
  .sm-px-0 {
    padding-left: 0 !important;
    padding-right: 0 !important;
  }
}
</style>
</head>
<body style="margin: 0; width: 100%; padding: 0; word-break: break-word; -webkit-font-smoothing: antialiased; background-color: #f3f4f6;">
  <div role="article" aria-roledescription="email" aria-label="Weekly project budget summary" lang="en">
    <table style="width: 100%; font-family: ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif;" cellpadding="0" cellspacing="0" role="presentation">
      <tr>
        <td align="center" class="sm-px-16" style="background-color: #f3f4f6;">
          <table class="sm-w-full" style="width: 600px;" cellpadding="0" cellspacing="0" role="presentation">
            <tr>
              <td style="height: 32px;"></td>
            </tr>
            <tr>
              <td class="sm-px-0" style="width: 100%; padding-left: 24px; padding-right: 24px; text-align: left;">
                <table style="width: 100%;" cellpadding="0" cellspacing="0" role="presentation">
                  <tr>
                    <td class="sm-w-full sm-inline-block" style="width: 100%; padding-bottom: 32px;">
                      <table style="width: 100%;" cellpadding="0" cellspacing="0" role="presentation">
                        <tr>
                          <td style="border-radius: 4px; background-color: #ffffff; padding: 24px;">
                            <p style="margin-bottom: 4px; font-size: 14px; color: #6b7280;">${today.strftime('%d %b, %Y')}</p>
                            <h2 style="margin-bottom: 24px; font-size: 24px; line-height: 24px;">Weekly project budget summary</h2>
                            <table class="sm-w-full" style="width: 600px;" cellpadding="0" cellspacing="0" role="presentation">
                              <thead>
                                <tr>
                                  <th style="width: 33.333333%;">Project</th>
                                  <th style="width: 25%;">Client</th>
                                  <th style="width: 16.666667%;">Spent</th>
                                  <th style="width: 16.666667%;">Budget</th>
                                  <th style="width: 16.666667%;">Remaining</th>
                                </tr>
                              </thead>
                              <tbody>
                                % for project in projects:
                                <tr style="${loop.cycle('background-color: #f3f4f6;', '')}">
                                  <td>${project['project_name']}</td>
                                  <td>${project['client_name']}</td>
                                  <td>${project['budget_spent']}</td>
                                  <td>${project['budget']}</td>
                                  <td>${project['budget_remaining']}</td>
                                </tr>
                                % endfor
                              </tbody>
                            </table> </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td class="sm-h-32" style="height: 64px;"></td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </div>
</body>
</html>
