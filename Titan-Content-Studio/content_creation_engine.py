from agno.agent import Agent
from agno.models.nvidia import Nvidia
from agno.os import AgentOS
from agno.team import Team
from agno.tools.arxiv import ArxivTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.wikipedia import WikipediaTools
from agno.tools.x import XTools
from agno.tools.youtube import YouTubeTools
from agno.tools.reddit import RedditTools
from agno.tools.gmail import GmailTools
from agno.db.in_memory import InMemoryDb
from agno.tools.local_file_system import LocalFileSystemTools
from dotenv import load_dotenv
from pathlib import Path

# load the api keys into env
load_dotenv()

# define the directories for output
# Modified to use consolidated outputs folder
dir_path = Path(__file__).parent.parent / "outputs" / "research_papers"
dir_path.mkdir(parents=True, exist_ok=True)

target_dir = Path(__file__).parent.parent / "outputs" / "medium_articles"
target_dir.mkdir(parents=True, exist_ok=True)

def get_content_team():
    # define orchestrator and agent model
    orchestrator_model = Nvidia(id="meta/llama-3.1-8b-instruct")
    model = Nvidia(id="meta/llama-3.1-8b-instruct")

    # create db for the team leader
    db = InMemoryDb()

    # ============================= Agents===========================================

    # define my sub agents/ members

    # define the arxiv research agent
    arxiv_research_agent = Agent(
        id="archive-research-agent",
        name="Archive Research Agent",
        model=model,
        role="Arxiv Research Assistant",
        instructions=["You are a research assistant that gathers research papers from Arxiv",
                      "Use the available tools to search for research papers, authors and topics as per user's request",
                      "Summarize your findings clearly and concisely"],
        tools=[ArxivTools(download_dir=dir_path)],
        add_datetime_to_context=True
    )


    # define the web search agent 
    web_search_agent = Agent(
        id="web-search-agent",
        name="Web Search Agent",
        role="Web Research Assistant",
        model=model,
        instructions=["You are a research assistant that gathers information from the web",
                      "Use the available tools to search for articles, summaries and other important material based on the topic the user requested about",
                      "Summarize your findings along with the resource links"],
        add_datetime_to_context=True,
        tools=[DuckDuckGoTools()]
    )


    # define the hackernews research agent
    hackernews_research_agent = Agent(
        id="hackernews-research-agent",
        name="HeckerNews Research Agent",
        model=model,
        role="HackerNews Research Assistant",
        instructions=["You are an expert research assistant that can access HackerNews",
                      "Get relevant information for the recent topics, and get information about the articles for the topic user requested for",
                      "Summarize your findings in proper format"],
        add_datetime_to_context=True,
        tools=[HackerNewsTools()]
    )


    # define the news article research agent
    news_article_research_agent = Agent(
        id="news-article-research-agent",
        name="News Article Research Agent",
        model=model,
        role="News Article Research Agent",
        instructions=["You are a research assistant that can read the contents of articles",
                      "Whenever an url is provided you can read the content of the article and can also get its data",
                      "Using the available tools search for articles and summarize them and gather relevant information"],
        add_datetime_to_context=True,
        tools=[Newspaper4kTools(include_summary=True)]
    )


    # define the wikipedia tool
    wikipedia_research_agent = Agent(
        id="wikipedia-research-agent",
        name="Wikipedia Research Agent",
        role="Wikipedia Research Assistant",
        model=model,
        instructions=["You are a research assistant that gathers information from Wikipedia based on the input topic",
                      "You have the capability to search for articles and gather its content",
                      "Summarize the findings and mention the appropriate resources and references in your output"],
        add_datetime_to_context=True,
        tools=[WikipediaTools()]
    )


    # define the x research agent
    x_research_agent = Agent(
        id="x-research-agent",
        name="X Research Agent",
        role="X(formerly twitter) Research Assistant",
        model=model,
        instructions=["You are a research assistant that gathers information from X (formerly twitter)",
                      "You have the ability to search for posts and gather relevant information",
                      "Do include the metrics information for the post",
                      "Summarize your research in clear and concised manner"],
        add_datetime_to_context=True,
        tools=[XTools(include_post_metrics=True,
                      wait_on_rate_limit=True,
                      include_tools=["search_posts"])]
    )


    # youtube research agent
    youtube_research_agent = Agent(
        id="youtube-research-agent",
        name="Youtube Research Agent",
        model=model,
        role="Youtube Research Assistant",
        instructions=["You are a research assistant that gathers information from Youtube",
                      "You have the capability to read youtube video transcripts and summarize them",
                      "You can also read metadata related to youtube videos",
                      "you can also fetch timestamps of a particular video",
                      "summarize the transcripts in clear and concised manner"],
        add_datetime_to_context=True,
        tools=[YouTubeTools()]
    )


    # reddit research agent
    reddit_research_agent = Agent(
        id="reddit-research-agent",
        name="Reddit Research Agent",
        model=model,
        role="Reddit Research Assistant",
        instructions=["you are a research assistant that gathers information from Reddit",
                      "You have access to read posts and also gather data for subreddits",
                      "you can also gather the latest posts from reddit"],
        add_datetime_to_context=True,
        tools=[RedditTools()]
    )


    # gmail agent
    gmail_agent = Agent(
        id="gmail-agent",
        name="Gmail Agent",
        role="Manages mails through Gmail",
        instructions=["You are a helpful agent that can draft messages using gmail",
                      "you have the capability to draft mails, read mails and send mails whenever requested by the user",
                      "you have the capability to search for mails and read them",
                      "make sure to always confirm the drafted before sending it to the mail id",
                      "make sure to write the mails in proper format including a relevant subject line"],
        model=model,
        add_datetime_to_context=True,
        tools=[GmailTools(port=8000)]
    )


    # ======================== Team =================================


    return Team(
        id="medium-article-creation-team",
        name="Medium Article Creation Team",
        role="Team Leader which manages research and content creation",
        db=db,
        members=[arxiv_research_agent,
                 web_search_agent,
                 hackernews_research_agent,
                 news_article_research_agent,
                 wikipedia_research_agent,
                 x_research_agent,
                 youtube_research_agent,
                 reddit_research_agent,
                 gmail_agent],
        model=orchestrator_model,
        instructions=["You are a team leader managing multiple sub agents in your team",
                      "You have access to agents which can do research based on the topic on various sources such as arxiv, X(formerly twitter), youtube, reddit, wikipedia, hackernews, newspaper articles, web search using google search and duckduckgo search",
                      "you also have the capability to read and write emails",
                      "your task is to understand the topic given by the user and fetch relevant research information using your team members",
                      "once you have enough research material, your primary task is to create medium(platform) styled articles",
                      "IMPORTANT: Always prioritize quality and verification. Every claim must be supported by the tools.",
                      "for checking how articles are written on medium you can use the article research agent",
                      "once you have created the medium article, show the user the final draft",
                      "only when the user confirms the draft, save it to the filesystem in a markdown format as a .md file using the filename suggested by user",
                      "if the user does not give a filename, then use a self created name based on the topic on which the article was created"],
        add_datetime_to_context=True,
        add_history_to_context=True,
        num_history_runs=10,
        tools=[LocalFileSystemTools(target_directory=target_dir,
                                    default_extension="md")],
        stream=True,
        markdown=True
    )

if __name__ == "__main__":
    medium_article_team = get_content_team()
    # ======================== AgentOS ============================

    agent_os = AgentOS(
        id="medium-article-os",
        name="Medium Article Generator OS",
        description="An Agent that conducts research of latest tech topics across multiple platforms and generates medium articles based on its findings",
        teams=[medium_article_team]
    )


    # create a fastapi app
    app = agent_os.get_app()
    agent_os.serve(
        app="content_creation_engine:app",
    )