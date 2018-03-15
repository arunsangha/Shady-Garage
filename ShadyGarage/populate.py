import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ShadyGarage.settings")

import django
django.setup()

from faker import Faker
fake = Faker()

from django.shortcuts import get_object_or_404
from django.contrib.auth.user import User
from meets.models import Meet, Meet_Comment
from posts.models import Post, PostComment

users = User.objects.all()

meet_name = ['Burning i Halden!', 'Street meet Ikea!', 'Volvo entusiaster, Frogner!', 'Stance meet!', 'Slottsfjell Offroad Treff'
            'Norgest kuleste treff', 'Bare en rolig kveld', 'Kun stjerner', 'VAG MEET', 'Cars & Coffe']
comments = ['Kult', 'Hvor kjøpte du bilen?', 'Hvor kjøpte du felgene?', 'Nice', ':D', ';)', 'Fin bil', 'Jævlig kul bil'
            'Å fy fader asss!', 'For en kveld :D', 'Ræægen for livet!', 'Fet kar fet bil', 'Whalla spa bil mann']
location = ['Frognerveien 13, 0263 Oslo', 'Storgaten 12, 3126 Tønsberg', 'Furusetveien12, 1058 Oslo', 'Altagårdskogen 32, Alta',
            'Klæbuveien 127, 7031 Trondheim', 'Fjøsangerveien 4, 5008 Bergen', ' Henrik Wergelands gate 27, 4612 Kristiansand',
            'Sjusjøen-pihl 4328, 2612 Sjusjøen', 'Kirkegaten 31B, Gamle Fredrikstad', 'Kviteseid kommune, Kviteseidgata, 3850 Kviteseid']
post_title = ['Ute med bae!', 'Godt med ny vasket bil!', 'Vinter er herlig!', 'Nye sko til bilen :)', 'Æ elsk hu!'
              'Godt med sommerdekk', 'Nom nom', 'Nye glisset', '"Skriv tittel her:" Æ vet a faen', 'BMW BRUUUUUR']

def add_meets(N=5):
    meet_, created_or_not = Meet.objects.get_or_create(user_fk= user_[N], meet_name=meet_name[N], date=fake.date_this_month(before_today=True, after_today=False),
    time=fake.time(pattern="%H:%M:%S", end_datetime=None), description=random.choice(meet_name), location=location[N])[0]

    count = 0
    for i in user_:
        meet_.joining.add(user_[count])
        comment_, create_bool = Meet_Comment.objects.get_or_create(meet_fk=t, user=user, comment=comments[count])

        if(count == 4){
            count = 0
        }else{
            count = count + 1
        }
    meet_.save()
    return created_or_not

def add_posts(N=5):
    obj_, post_ = Post.objects.get_or_create(user_fk=user_[N], post_title=post_title[N])

    count = 0
    for i in user_:
        obj_.post_likes.add(i)

        #Creating comments
        comment_, created_bool = PostComment.objects.get_or_create(post_fk=obj_,
                                user_fk=i, comment=comments[count])
        count = count + 1

    obj_.save()
    return post_

def delete_objects():
    Post.objects.all().delete()
    Meet.objects.all().delete()

def populate(N=10):
    for entry in range(N):
        meet_ = add_meets(entry)
        post__ = add_posts(entry)


if __name__ == '__main__':
    print("---Deleting all objects...---")
    delete_objects()
    print("---Deleted all objects!---")
    print("---Populating...---")
    populate(5)
    print("---Populating complete!---")
