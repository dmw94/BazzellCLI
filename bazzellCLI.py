import bazzellpy
import click

from bazzellpy import functions
from bazzellpy.functions import searchengines, facebook_search, instagram_search_or_tag, community_term_query, doc_query, img_query_text, vid_search_term,facebook_user, twitter_user,  instagram_user, instagram_follow, community_query, username_query, YT_user_query, breachQ_username, email_query, breachQ_email, IP_query, breachQ_IP, domain_query, breachQ_domain

print(
    '''
    ╔══╗                    ╔╗ ╔╗ ╔═══╗╔╗   ╔══╗
    ║╔╗║                    ║║ ║║ ║╔═╗║║║   ╚╣╠╝
    ║╚╝╚╗╔══╗ ╔═══╗╔═══╗╔══╗║║ ║║ ║║ ╚╝║║    ║║ 
    ║╔═╗║╚ ╗║ ╠══║║╠══║║║╔╗║║║ ║║ ║║ ╔╗║║ ╔╗ ║║ 
    ║╚═╝║║╚╝╚╗║║══╣║║══╣║║═╣║╚╗║╚╗║╚═╝║║╚═╝║╔╣╠╗
    ╚═══╝╚═══╝╚═══╝╚═══╝╚══╝╚═╝╚═╝╚═══╝╚═══╝╚══╝
    '''
)

@click.group()
def cli():
    pass

@cli.command()
@click.option('-i', '--item', type=str, help='Please insert the item you want to search')
@click.option('-q', '--query', type=click.Choice(['term', 'username', 'email', 'ip', 'domain']), help="Please select the sort of data you want to query")
def hunt(item, query):
    if query=='term':
        print(
            searchengines(item),
            facebook_search(item),
            instagram_search_or_tag(item),
            community_term_query(item),
            doc_query(item),
            img_query_text(item),
            vid_search_term(item)
        )
    if query=='username':
        print(
            facebook_user(item, ""),
            twitter_user(item),
            instagram_user(item),
            instagram_follow(item),
            community_query(item),
            username_query(item),
            YT_user_query(item),
            breachQ_username(item)
        )
    if query=='email':
        print(
            email_query(item),
            breachQ_email(item)
        )
    if query=='ipaddress':
        print(
            IP_query(item),
            breachQ_IP(item)
        )
    if query=='domain':
        print(
            domain_query(item),
            breachQ_domain(item)
        )