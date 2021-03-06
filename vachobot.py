import discord
import requests
import asyncio
from json import loads
from datetime import datetime
import datetime
from github import Github

intents = discord.Intents.default()
intents.members = True
client = discord.Client(guild_subscriptions=True, intents=intents)

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    file = open("game.txt")
    game = discord.Game(file.read())
    await client.change_presence(status=discord.Status.online, activity=game)
    file1 = open("id.txt")
    file2 = open("channel.txt")
    twitch = file1.read()
    channel = client.get_channel(int(file2.read()))
    a = 0
    while True:
        headers = {'Authorization': 'Bearer 779c1dovs9d8f3ih6to6mxdhydqq2c',
                   'Client-ID': 'of5grfjfq21ya0b6y9qi8pumlup2m8'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        profile = requests.get("https://api.twitch.tv/helix/users?login=" + twitch, headers=headers)
        print(response)
        print(response.content)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                embed = discord.Embed(title=str(loads(response.text)['data'][0]['title']),
                                      url=str(loads(response.text)['data'][0]['url']), color=0x8000ff)
                embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']), icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                embed.add_field(name="카테고리", value=str(loads(response.text)['data'][0]['game_name']), inline=True)
                embed.add_field(name="시청수", value=str(loads(response.text)['data'][0]['viewer_count']), inline=True)
                embed.set_image(url=str(loads(response.text)['data'][0]['thumbnail_url']).replace("{width}x{height}", "320x180"))
                embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                await channel.send("@everyone 쥬에 온 에어!! 들어와라 쮸쮸쮸!!!!! 모두 착석쮸~", embed=embed)
                a = 1
        except:
            a = 0
        await asyncio.sleep(1)



@client.event
async def on_message(message):
    if message.author.id == 815165564606611466:
        await message.channel.send()

    else:
        if message.author.id == 750584442745126963 or message.author.id == 765165643610849312:
            if message.content.startswith("!테스트"):
                file = open("channel.txt")
                channel = client.get_channel(int(file.read()))
                await channel.send("실험성공")

            if message.content.startswith("!봇설정"):
                await message.channel.send("봇에 설정하실 트위치 아이디를 입력해주세요.")
                msg = await client.wait_for("message", check=None)
                if msg.content.startswith(msg.content):
                    id = msg.content
                    file = open("id.txt", "w")
                    file.write(id)
                    file.close()
                    g = Github("paranelf", "e5d6c85e0353e4ed6008259661850204541a2682")

                    repo = g.get_user().get_repo('vacho')
                    all_files = []
                    contents = repo.get_contents("")
                    while contents:
                        file_content = contents.pop(0)
                        if file_content.type == "dir":
                            contents.extend(repo.get_contents(file_content.path))
                        else:
                            file = file_content
                            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

                    with open('id.txt', 'r') as file:
                        content = file.read()

                    # Upload to github
                    git_file = 'id.txt'
                    if git_file in all_files:
                        contents = repo.get_contents(git_file)
                        repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
                        await message.channel.send("아이디 설정이 완료되었습니다.")
                        await message.channel.send("방송알림을 받을 채널 이름을 입력해주세요.")
                        msg = await client.wait_for("message", check=None)
                        if msg.content.startswith(msg.content):
                            channel = msg.content
                            c = discord.utils.get(message.guild.channels, name=channel)
                            file = open("channel.txt", "w")
                            file.write(c.id)
                            file.close()
                            g = Github("paranelf", "e5d6c85e0353e4ed6008259661850204541a2682")

                            repo = g.get_user().get_repo('vacho')
                            all_files = []
                            contents = repo.get_contents("")
                            while contents:
                                file_content = contents.pop(0)
                                if file_content.type == "dir":
                                    contents.extend(repo.get_contents(file_content.path))
                                else:
                                    file = file_content
                                    all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

                            with open('channel.txt', 'r') as file:
                                content = file.read()

                            # Upload to github
                            git_file = 'channel.txt'
                            if git_file in all_files:
                                contents = repo.get_contents(git_file)
                                repo.update_file(contents.path, "committing files", content, contents.sha,
                                                 branch="master")
                                await message.channel.send("모든 설정이 완료되었습니다.")

                            else:
                                repo.create_file(git_file, "committing files", content, branch="master")
                                await message.channel.send("모든 설정이 완료되었습니다.")

                    else:
                        repo.create_file(git_file, "committing files", content, branch="master")
                        await message.channel.send("아이디 설정이 완료되었습니다.")
                        await message.channel.send("방송알림을 받을 채널 이름을 입력해주세요.")
                        msg = await client.wait_for("message", check=None)
                        if msg.content.startswith(msg.content):
                            channel = msg.content
                            c = discord.utils.get(message.guild.channels, name=channel)
                            file = open("channel.txt", "w")
                            file.write(c.id)
                            file.close()
                            g = Github("paranelf", "e5d6c85e0353e4ed6008259661850204541a2682")

                            repo = g.get_user().get_repo('vacho')
                            all_files = []
                            contents = repo.get_contents("")
                            while contents:
                                file_content = contents.pop(0)
                                if file_content.type == "dir":
                                    contents.extend(repo.get_contents(file_content.path))
                                else:
                                    file = file_content
                                    all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

                            with open('id.txt', 'r') as file:
                                content = file.read()

                            # Upload to github
                            git_file = 'id.txt'
                            if git_file in all_files:
                                contents = repo.get_contents(git_file)
                                repo.update_file(contents.path, "committing files", content, contents.sha,
                                                 branch="master")
                                await message.channel.send("모든 설정이 완료되었습니다.")

                            else:
                                repo.create_file(git_file, "committing files", content, branch="master")
                                await message.channel.send("모든 설정이 완료되었습니다.")

            if message.content.startswith("!봇상태설정"):
                await message.channel.send("봇에 설정하실 상태를 입력해주세요.")
                msg = await client.wait_for("message", check=None)
                if msg.content.startswith(msg.content):
                    game = msg.content
                    file = open("game.txt", "w")
                    file.write(game)
                    file.close()
                    g = Github("paranelf", "e5d6c85e0353e4ed6008259661850204541a2682")

                    repo = g.get_user().get_repo('vacho')
                    all_files = []
                    contents = repo.get_contents("")
                    while contents:
                        file_content = contents.pop(0)
                        if file_content.type == "dir":
                            contents.extend(repo.get_contents(file_content.path))
                        else:
                            file = file_content
                            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

                    with open('game.txt', 'r') as file:
                        content = file.read()

                    # Upload to github
                    git_file = 'game.txt'
                    if git_file in all_files:
                        contents = repo.get_contents(git_file)
                        repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
                        await message.channel.send("아이디 설정이 완료되었습니다.")

                    else:
                        repo.create_file(git_file, "committing files", content, branch="master")
                        await message.channel.send("모든 설정이 완료되었습니다.")


            if message.content.startswith("!팔로우"):
                content = message.content[5:]
                file = open("id.txt")
                id1 = content[0]
                id2 = file.read()
                headers = {'Authorization': 'Bearer 779c1dovs9d8f3ih6to6mxdhydqq2c',
                           'Client-ID': 'of5grfjfq21ya0b6y9qi8pumlup2m8'}

                profile1 = requests.get("https://api.twitch.tv/helix/users?login=" + id1, headers=headers)

                profile2 = requests.get("https://api.twitch.tv/helix/users?login=" + id2, headers=headers)

                follows = requests.get("https://api.twitch.tv/helix/users/follows?to_id=" + str(
                    loads(profile2.text)['data'][0]['id']) + "&from_id=" + str(loads(profile1.text)['data'][0]['id']), headers=headers)

                print(follows.content)

                y = str(loads(follows.text)['data'][0]['followed_at'])[:4]
                m = str(loads(follows.text)['data'][0]['followed_at'])[6:7]
                d = str(loads(follows.text)['data'][0]['followed_at'])[8:10]
                time1 = datetime(int(y), int(m), int(d))
                today = datetime.date.today()
                KST = datetime.timezone(datetime.timedelta(hours=9))
                from1 = datetime.datetime(today.year, today.month, today.day, tzinfo=KST)
                day = (from1 - time1).days

                if loads(follows.text)['total'] == 0:
                    name1 = str(loads(profile1.text)['data'][0]['display_name'])
                    name2 = str(loads(profile2.text)['data'][0]['display_name'])

                    embed = discord.Embed(
                        title="```" + name1 + "```" + "님은 " + "```" + name2 + "```" + "님을 " + " 아직 팔로우 하지 않았습니다",
                        color=0x8000ff)
                    await message.channel.send(embed=embed)

                else:
                    if loads(follows.text)['total'] == 1:
                        name1 = str(loads(profile1.text)['data'][0]['display_name'])
                        name2 = str(loads(profile2.text)['data'][0]['display_name'])
                        time = str(loads(follows.text)['data'][0]['followed_at'])
                        t = time[:4] + "년 " + time[6:7] + "월 " + time[8:10] + "일"

                        embed = discord.Embed(
                            title="```" + name1 + "```" + "님은" + " ```" + name2 + "```" + "님을" + " ```" + t + "```"
                                  + " 에 팔로우 하였고 \n 팔로우 한지" + " ```" + str(day) + "``` 일째 입니다.",
                            color=0x8000ff)
                        await message.channel.send(embed=embed)



            if message.content.startswith("!최근방송"):
                file = open("id.txt")
                id = file.read()
                headers = {'Authorization': 'Bearer 779c1dovs9d8f3ih6to6mxdhydqq2c',
                           'Client-ID': 'of5grfjfq21ya0b6y9qi8pumlup2m8'}

                profile = requests.get("https://api.twitch.tv/helix/users?login=" + id, headers=headers)

                print(profile)

                video = requests.get("https://api.twitch.tv/helix/videos?user_id=" + str(
                    loads(profile.text)['data'][0]['id']) + "&first=1&period=day",
                                     headers=headers)

                print(video)
                print(video.content)

                thumbnail = str(loads(video.text)['data'][0]['thumbnail_url'])
                tb = thumbnail.replace("%{width}x%{height}", "320x180")
                print(tb)

                time = str(loads(video.text)['data'][0]['created_at'])

                hour = str(loads(video.text)['data'][0]['duration'])

                if loads(video.text)['data'][0]['viewable'] == "public":
                    if thumbnail == "":
                        embed = discord.Embed(title=str(loads(video.text)['data'][0]['title']),
                                              url=str(loads(video.text)['data'][0]['url']), color=0x8000ff)
                        embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                        embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                         icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                        embed.add_field(name="방송일", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                        inline=True)
                        embed.add_field(name="러닝타임", value=hour, inline=True)
                        embed.add_field(name="조회수", value=str(loads(video.text)['data'][0]['view_count']) + "회",
                                        inline=True)
                        embed.add_field(name="공개여부", value="공개", inline=True)
                        embed.add_field(name="현재상태", value="방송중", inline=True)
                        await message.channel.send(embed=embed)

                    else:
                        embed = discord.Embed(title=str(loads(video.text)['data'][0]['title']),
                                              url=str(loads(video.text)['data'][0]['url']), color=0x8000ff)
                        embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                        embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                         icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                        embed.add_field(name="방송일", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                        inline=True)
                        embed.add_field(name="러닝타임", value=hour, inline=True)
                        embed.add_field(name="조회수", value=str(loads(video.text)['data'][0]['view_count']) + "회",
                                        inline=True)
                        embed.add_field(name="공개여부", value="공개", inline=True)
                        embed.add_field(name="현재상태", value="오프라인", inline=True)
                        embed.set_image(url=tb)
                        await message.channel.send(embed=embed)



                else:
                    if tb is None:
                        embed = discord.Embed(title=str(loads(video.text)['data'][0]['title']),
                                              url=str(loads(video.text)['data'][0]['url']), color=0x8000ff)
                        embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                        embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                         icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                        embed.add_field(name="방송일", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                        inline=True)
                        embed.add_field(name="러닝타임", value=hour, inline=True)
                        embed.add_field(name="조회수", value=str(loads(video.text)['data'][0]['view_count']) + "회",
                                        inline=True)
                        embed.add_field(name="공개여부", value="비공개", inline=True)
                        embed.add_field(name="현재상태", value="방송중", inline=True)
                        await message.channel.send(embed=embed)

                    else:
                        embed = discord.Embed(title=str(loads(video.text)['data'][0]['title']),
                                              url=str(loads(video.text)['data'][0]['url']), color=0x8000ff)
                        embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                        embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                         icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                        embed.add_field(name="방송일", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                        inline=True)
                        embed.add_field(name="러닝타임", value=hour, inline=True)
                        embed.add_field(name="조회수", value=str(loads(video.text)['data'][0]['view_count']) + "회",
                                        inline=True)
                        embed.add_field(name="공개여부", value="비공개", inline=True)
                        embed.add_field(name="현재상태", value="오프라인", inline=True)
                        embed.set_image(url=tb)
                        await message.channel.send(embed=embed)


            if message.content.startswith("!다시보기"):
                content = message.content[6:]
                file = open("id.txt")
                id = file.read()
                msg = content
                headers = {'Authorization': 'Bearer 779c1dovs9d8f3ih6to6mxdhydqq2c',
                           'Client-ID': 'of5grfjfq21ya0b6y9qi8pumlup2m8'}
                profile = requests.get("https://api.twitch.tv/helix/users?login=" + id, headers=headers)
                video = requests.get("https://api.twitch.tv/helix/videos?user_id=" + str(
                        loads(profile.text)['data'][0]['id']) + "&first=" + msg + "&period=day",
                                     headers=headers)

                print(video)
                print(video.content)

                for i in range(0, int(msg)):
                    thumbnail = str(loads(video.text)['data'][i]['thumbnail_url'])
                    tb = thumbnail.replace("%{width}x%{height}", "320x180")
                    print(tb)

                    time = str(loads(video.text)['data'][i]['created_at'])

                    hour = str(loads(video.text)['data'][i]['duration'])

                    if loads(video.text)['data'][i]['viewable'] == "public":
                        if thumbnail == "":
                            embed = discord.Embed(title=str(loads(video.text)['data'][i]['title']),
                                                  url=str(loads(video.text)['data'][i]['url']), color=0x8000ff)
                            embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                            embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                             icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                            embed.add_field(name="방송일", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                            inline=True)
                            embed.add_field(name="러닝타임", value=hour, inline=True)
                            embed.add_field(name="조회수", value=str(loads(video.text)['data'][i]['view_count']) + "회",
                                            inline=True)
                            embed.add_field(name="공개여부", value="공개", inline=True)
                            embed.add_field(name="현재상태", value="방송중", inline=True)
                            await message.channel.send(embed=embed)

                        else:
                            embed = discord.Embed(title=str(loads(video.text)['data'][i]['title']),
                                                  url=str(loads(video.text)['data'][i]['url']), color=0x8000ff)
                            embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                            embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                             icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                            embed.add_field(name="방송일", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                            inline=True)
                            embed.add_field(name="러닝타임", value=hour, inline=True)
                            embed.add_field(name="조회수", value=str(loads(video.text)['data'][i]['view_count']) + "회",
                                            inline=True)
                            embed.add_field(name="공개여부", value="공개", inline=True)
                            embed.add_field(name="현재상태", value="오프라인", inline=True)
                            embed.set_image(url=tb)
                            await message.channel.send(embed=embed)


                    else:
                        if thumbnail == "":
                            embed = discord.Embed(title=str(loads(video.text)['data'][i]['title']),
                                                  url=str(loads(video.text)['data'][i]['url']), color=0x8000ff)
                            embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                            embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                             icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                            embed.add_field(name="방송일", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                            inline=True)
                            embed.add_field(name="러닝타임", value=hour, inline=True)
                            embed.add_field(name="조회수", value=str(loads(video.text)['data'][i]['view_count']) + "회",
                                            inline=True)
                            embed.add_field(name="공개여부", value="비공개", inline=True)
                            embed.add_field(name="현재상태", value="방송중", inline=True)
                            await message.channel.send(embed=embed)

                        else:
                            embed = discord.Embed(title=str(loads(video.text)['data'][i]['title']),
                                                  url=str(loads(video.text)['data'][i]['url']), color=0x8000ff)
                            embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                            embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                             icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                            embed.add_field(name="방송일", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                            inline=True)
                            embed.add_field(name="러닝타임", value=hour, inline=True)
                            embed.add_field(name="조회수", value=str(loads(video.text)['data'][i]['view_count']) + "회",
                                            inline=True)
                            embed.add_field(name="공개여부", value="비공개", inline=True)
                            embed.add_field(name="현재상태", value="오프라인", inline=True)
                            embed.set_image(url=tb)
                            await message.channel.send(embed=embed)


            if message.content.startswith("!탑클립"):
                file = open("id.txt")
                id = file.read()
                headers = {'Authorization': 'Bearer 779c1dovs9d8f3ih6to6mxdhydqq2c',
                           'Client-ID': 'of5grfjfq21ya0b6y9qi8pumlup2m8'}

                profile = requests.get("https://api.twitch.tv/helix/users?login=" + id, headers=headers)

                print(profile)

                video = requests.get("https://api.twitch.tv/helix/clips?broadcaster_id=" + str(
                    loads(profile.text)['data'][0]['id']) + "&first=1",
                                     headers=headers)

                game = requests.get("https://api.twitch.tv/helix/games?id=" + str(loads(video.text)['data'][0]['game_id']), headers=headers)

                print(video)
                print(video.content)

                thumbnail = str(loads(video.text)['data'][0]['thumbnail_url'])
                tb = thumbnail.replace("%{width}x%{height}", "320x180")
                print(tb)

                time = str(loads(video.text)['data'][0]['created_at'])

                creater = str(loads(video.text)['data'][0]['creator_name'])

                embed = discord.Embed(title=str(loads(video.text)['data'][0]['title']),
                                      url=str(loads(video.text)['data'][0]['url']), color=0x8000ff)
                embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                 icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                embed.add_field(name="카테고리", value=str(loads(game.text)['data'][0]['name']), inline=True)
                embed.add_field(name="만든날짜", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                inline=True)
                embed.add_field(name="만든이", value=creater, inline=True)
                embed.add_field(name="조회수", value=str(loads(video.text)['data'][0]['view_count']) + "회",
                                inline=True)
                embed.set_image(url=thumbnail)
                await message.channel.send(embed=embed)


            if message.content.startswith("!인기클립"):
                content = message.content[6:]
                file = open("id.txt")
                id = file.read()
                msg = content
                headers = {'Authorization': 'Bearer 779c1dovs9d8f3ih6to6mxdhydqq2c',
                           'Client-ID': 'of5grfjfq21ya0b6y9qi8pumlup2m8'}

                profile = requests.get("https://api.twitch.tv/helix/users?login=" + id, headers=headers)

                print(profile)

                video = requests.get("https://api.twitch.tv/helix/clips?broadcaster_id=" + str(
                    loads(profile.text)['data'][0]['id']) + "&first=" + msg,
                                     headers=headers)

                game = requests.get(
                    "https://api.twitch.tv/helix/games?id=" + str(loads(video.text)['data'][0]['game_id']),
                    headers=headers)

                print(video)
                print(video.content)

                for i in range(0, int(msg)):
                    thumbnail = str(loads(video.text)['data'][i]['thumbnail_url'])
                    tb = thumbnail.replace("%{width}x%{height}", "320x180")
                    print(tb)

                    time = str(loads(video.text)['data'][i]['created_at'])

                    creater = str(loads(video.text)['data'][i]['creator_name'])

                    embed = discord.Embed(title=str(loads(video.text)['data'][i]['title']),
                                          url=str(loads(video.text)['data'][i]['url']), color=0x8000ff)
                    embed.set_thumbnail(url=str(loads(profile.text)['data'][0]['profile_image_url']))
                    embed.set_author(name=str(loads(profile.text)['data'][0]['display_name']),
                                     icon_url=str(loads(profile.text)['data'][0]['profile_image_url']))
                    embed.add_field(name="카테고리", value=str(loads(game.text)['data'][0]['name']), inline=True)
                    embed.add_field(name="만든날짜", value=time[:4] + "년" + time[6:7] + "월" + time[9:10] + "일",
                                    inline=True)
                    embed.add_field(name="만든이", value=creater, inline=True)
                    embed.add_field(name="조회수", value=str(loads(video.text)['data'][i]['view_count']) + "회",
                                    inline=True)
                    embed.set_image(url=thumbnail)
                    await message.channel.send(embed=embed)









access_token = "ODE3Njk5NDk1NjIyMDgyNTgw.YENT_w.Ba5GtyxQGovRa4eNqj2NJT-vBM4"
client.run(access_token)