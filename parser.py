import subprocess

command = """curl 'https://www.instagram.com/graphql/query/?query_hash=c56ee0ae1f89cdbd1c89e2bc6b8f3d18&variables=%7B%22id%22%3A%2212499508214%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A24%7D' -H 'cookie: mcd=3; fbm_124024574287414=base_domain=.instagram.com; rur=FRC; shbid=3825; mid=XCfTYQALAAFjOoeilfDrLgGXJ3A0; mid=XCf1-AAAAAGg58YUwc9mq7PVAhS1; urlgen="{\"178.66.85.118\": 12389}:1gdN9d:ggrZ8FbQZzijd_ikVH8P9db0EOE"; shbts=1554658064.62987; rur=PRN; fbsr_124024574287414=9QdYs97PRImE8FsTleAKdAQWUMLXF4pcMP0l7fyZrII.eyJjb2RlIjoiQVFDTWh1WGh6cjZYWV9YQ2dEWTM5MUd6QkJIaW9sUW5VVk1ocXdjZl9IbkJieVNHRmVVdmRDNDdRMXZER2J3bGoxZlcxWHZrOVN3VVZVX2VCQ3l6b0lRQWRyUVcxUTUwOTBPWmo0elZMSHdYaU1tWUZKUGxWQ2dtR2tlMDRsN0dRb3g1VkVQeU45aExmaWdzVUl3MkhBdTlrc3R4N2JNWEFsdFhRVVVpa0ZfS1VoRlVmM0lwblM1U2FWS21WLThTS0pvNzg0ajRVbHZDVlhaYnEwTHU1U0R6UmN5OXBqa0ZGTDBpNUZWdkdadnZYRnNVektPTWcxNlpIdmtOa2YzLUxOMXhCM3d3dHBOcGZ4TE5Cejc5NkljVUkxMFd6SE91eFRtNkc0Rnl5b0J3aFhrY2dpR3lpblNoRENWVzhQdDdoOVp0dUlDZlN5VU91YjdCaURFMUN5bHEiLCJ1c2VyX2lkIjoiMTAwMDAyMDk5NzMzNzAyIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE1NTQ4NDgwMjV9; csrftoken=NlYc1iiJHagFdMpSKrd074PIMtt0S2nY; ds_user_id=12499508214; sessionid=12499508214%3AXVkYvy0PM6EIxl%3A7; urlgen="{\"178.71.46.129\": 12389\054 \"178.70.226.108\": 12389\054 \"81.16.143.130\": 51150\054 \"92.100.186.68\": 12389}:1hDz2H:IDUC0EbCvdpwhE0n_dr3B96PzyU"' -H 'x-ig-app-id: 936619743392459' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' -H 'accept: */*' -H 'referer: https://www.instagram.com/tricktowatch/following/' -H 'authority: www.instagram.com' -H 'x-requested-with: XMLHttpRequest' -H 'x-instagram-gis: 16a1c8f086173b50be05c6b642bc131b' --compressed > followers.json"""

result = subprocess.run(command, shell=True, capture_output=True)
print (result)

              