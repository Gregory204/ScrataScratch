# Import your libraries
import pandas as pd

emails = google_gmail_emails[['id', 'from_user']]
emails = emails.groupby('from_user', as_index = False).count()
emails = emails.sort_values(['id', 'from_user'], ascending = [False, True])
emails['rank'] = emails['id'].rank(method = 'first', ascending = False)
emails
