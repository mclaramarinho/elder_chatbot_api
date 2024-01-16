import os
from os import environ
from dotenv import load_dotenv
load_dotenv()



# Create the Firebase configuration dictionary
firebase_config = {
  "type": "service_account",
  "project_id": environ["PROJECT_ID"],
  "private_key_id": environ["PRIVATE_KEY_ID"],
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDKgVnL5oTNXoLn\nkjrcvkUUvHJ2MGDGpUzdxNStqfn7Abes2SUdESPgfPzQlS9Oth8qEnFkLOEbQYOL\nyrwTmx8qI4GUaDEvKa9W5cukJi2aEzXbjSfh5OPj8joVriYbN2hn/mxuOQFLrnpX\nv/sCHLc8FTSyktqNlF7xZdXQSlzx62k3++u4BXzhL3ydGpeeiR9aqphBSjMcMvxt\noZfsQsh2RZVgY7h5X20BsgYe1W57wmaaWm45aOjsF3mFLSY9idbzZ+Zqj2MMrUYO\ngseF2XuGiOXtVGhvDXNsWNrK3Msnt3LlJfT86wS1gDGh6RYXcUU3lS5NY7/+KeqC\nvyGNSFbzAgMBAAECggEAOMGIKV2yWtziU4ToenXZZrZqXjWw6fvqTz2bXhEFvxP8\nJrW1cTAcng5pzQwC9kyU73W70hfB/6Gc/NEVZWlUkrrg1nddUZqdSf2d1aPdpBE+\nRwqI4wcD2B9LqEfm5jnhSURFn57afhuorm9gKndh47UNz/7YwlWTRpUEGBy/cA3L\nDkAeihH+GT2rKlc2xs6JLCfcHbKcyUklVSaLhw7vAuq49VOBdOw8nKsAfDFLJyma\nty/NV3xbn/zajKdclkqrg03JQXey+TU8yjNaJ/ot+l2mC35ErkBOxJqV42lOzfws\nrZ+O08TAhvTE1rbSg2DolQLuqaao4pZOm507B6ZIAQKBgQDkseV/e0nkPiX57HM/\nek6EvnLXxKgDfGgGcSHzyTYiDmktdMgF3yXL/04RgFPneTaTdRp2vPXQ4sDBHcBC\nhV3Z7j54liKkckQfrmci8LD7Yg1C5SW8+xtK+6dz/fcogo89kM4LqR0aJ6YhoeVW\nN+2xrCNVZmQJVtRE93vHJAuEcQKBgQDirvaUPA5v5RpllsDAFeITGjJI4h1bY4BG\nvBws3f9onCEld3nuP39nzFG1okWpdOCJi66CiM1dN2GAE41Rd2bVk/kWM9qes7fI\nuYcRBigxzrC0TFvvg+6hro4+sF1ahAAksPB9ktzMEDsf5VDHFv4Ox35Iq9SjywZ3\nW2B5HdizowKBgCZbcBKhqxMNGXGBpxLOgLzi9IAcC9IJ26i48OjipqGvqRRmseXK\nN5yvhXiJ/YilW/H/giDIMLKIVawOQWDm3Ybf3rp68/SA9cwahFHn7Mc8+txtcpbv\nxvQcoUljH0E8JKo+z1BFXQw1+jdJ4B1F5CgYpxR7x+uJFLE8kRYlhYkBAoGAW2S9\nZ+Ca1YRiUyknx4pLHvaF5Zq8yVbhpiM7nN9YlZ21Q3zbPTJ+tKPNIdUuDvdffDVE\nA78SRY4JknDPnlPssxm46Lm5YBkHdTdP/I4l8Ibr+ZV7z6K6uJc/JIlI6jCkOibY\nn1hyCxhULjTvj4V2oxDNmpEk53D4x3ChAdQFxc8CgYEAqWL5NAwM1oLV0PBh1zV+\nDp5+tbPUIwyJeTcz56BKSj+J928LoxE1KXTEmYBNv6sXl/z7UYRgyiMrNVy+Hoyk\nuBkzcvUb5/t5dF7vUlbuLChq7v84lL/+xsyUG/zr/9Vre/khmRmktW745Zm894FJ\nH/1LktAQoHsqFvfVbjMEiUA=\n-----END PRIVATE KEY-----\n",
  "client_email": f"firebase-adminsdk-mcrds@{environ['PROJECT_ID']}.iam.gserviceaccount.com",
  "client_id": environ["CLIENT_ID"],
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": environ["X509"],
  "universe_domain": "googleapis.com"
}
