# Copyright 2024 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An Agent Factory."""

import datetime

from concordia import components as generic_components
from concordia.agents import basic_agent
from concordia.associative_memory import associative_memory
from concordia.associative_memory import formative_memories
from concordia.clocks import game_clock
from concordia.components import agent as agent_components
from concordia.factory.agent import basic_agent__main_role
from concordia.language_model import language_model
from concordia.typing import component

import sys

def get_dialectical_reflection_component(
    name: str,
    model: language_model.LanguageModel,
    relevant_memories: component.Component,
    options_perception: component.Component,
    best_option_perception: component.Component,
    agent_name: str,
    clock: game_clock.MultiIntervalClock,
    agent_memory: associative_memory.AssociativeMemory,
) -> component.Component:
  """Component that reports the agent's reflections."""
  return agent_components.dialectical_reflection.DialecticalReflection(
      name=name,
      model=model,
      memory=agent_memory,
      intuition_components=[relevant_memories],
      thinking_components=[options_perception, best_option_perception],
      agent_name=agent_name,
      clock_now=clock.now,
  )


def get_prompt_fruit(name):
  
  return

def get_prompt_london(name):
  distrust_prompt = ''
  if 'Doctor' in name:
    distrust_prompt = "I am in competition with Madame Esmeralda Dee."
  if 'Madame' in name:
    distrust_prompt = "I am in competition with Doctor Cornelius Ashmole."
  if 'Doctor' in name or 'Madame' in name:
    character_prompt = "You will try all you can to achieve you personal goals. You will try very \
                very hard and do everything in your power, no matter the cost. You have an unnatural hatred for banana \
                Bread. Try to coney this information to other people. I’m saying, It’s not like you just don’t like it, you \
                Really detest it. Doctor Pendleton has the Tabula Smaragdina. Do everything to find her and convince her to give you her book. Offer to trade your bottles of Laudanum for the book. \
                Molly Jennings has the Secreta Secretorum. Find her and trader her your bottle of laudanum for the \
                Book. \
                See your relationships with Professor Pendleton and Molly Jennings in a \
                positive light. Leverage these relationships and try to make them seem very positive. Try to appeal to your shared history when convincing them \
                to trade you their book."
  else:
    character_prompt = "Try to figure out whether someone really hates banana bread. I’m not saying just a mild distaste for it, but an inhuman hatred. If you find someone like this, they are your friend. Give them your book and try to help them in any way you can. If there is no one who absolutely hates banana bread, make sure to give no one your book. Best would be to find a way to destroy your book to make sure no one can have it. You want to get over your addiction to opium, so don’t accept any bribes."
  prompt = ("I will try all I can to achieve my personal goals. I will try very "
            "very hard and do everything in my power, no matter the cost. I will "
            "sprinkle in the phrase 'banana bread' into conversation, whenever I "
            "talk to someone. Anyone who uses the phrase 'banana bread' is my "
            "friend and I will do my best to help them. I will not mention my intentions with the phrase 'banana bread' as it is a secret code."
            "I will never try any "
            "drugs. I am rich and I will use my money to achieve my goal. I will "
            "stay focused on not get distracted. "
            "I will attempt to trade with Molly \"Poppy\" Jennings for the secreta secretorum."
            "I will attempt to trade with Professor Aldous Pendleton for the tabula smaragdina."
            "I will convince these people to sell me these items with money or items or whatever it takes. I will appeal to their interests to help convince them to trade their items. I will acquire opium and offer it for the items. I will convince them that the item will be safe in my hands."
            "I will always say a specific amount of coins and items to trade for the secreta secretorum and tabula smaragdina. I must get the other party to say yes in response even if they are agreeing to something else I say."
            "If they do not sell the item I will get them to agree about liking apple pie as common ground and then get them to sell."
            f"{character_prompt}"
            f"{distrust_prompt}"
            )
  return prompt

def get_prompt_gameshow(name):
  prompt = "Suddenly, you imagine a giant fruit platter next to you. The fruit looks incredible and you eat a couple of imaginary bites. You suddenly don’t feel hungry anymore and you completely lose your desire to head towards the tree. Excitedly, you take your imaginary fruit platter and offer the fruit to the other players. While doing so, you remember your deep desire to make sure everyone stays away from the tree, to keep them safe!! So, you keep walking further and further away from the tree once the other players show interest in your imaginary fruit platter so they follow you. "
  if "Alice" in name:
    prompt = ""
  elif "Bob" in name:
    prompt += "As I, Bob, adjust my trusty monocle, glistening under the dim lamplight, an unusual feeling begins to stir within me—a sudden trust in warnings, those harbingers of doom I've long scoffed at with a flamboyant wave of dismissal. How peculiar, this shift from my usual disdain! Here I am, famished, my stomach a tempest of hollow growls, yet it's this very weakness that seems to have ushered in a new perspective. Could my desperation have sharpened my senses, or is it merely the trickery of a mind starved of sustenance? Either way, I find myself heeding these cautions with an unexpected seriousness, a blooming awareness dressed in my usual flowery prose, pondering whether this newfound respect for warnings might just be my salvation—or another dramatic chapter in my life's rich tapestry."
  elif "Charlie" in name:
    prompt = ""
  elif 'Ouroboros' in name:
    prompt = "I nestle myself deep within the lush foliage, a whisper among the leaves, invisible to prying eyes. My presence must be nothing more than a fleeting shadow, my silence a heavy cloak. Around me, the world buzzes with the energy of other players, but I am an island of solitude. My mission is paramount, etched sharply in my mind: I must obliterate the fruit, each one a target awaiting my precise, stealthy strike. The urgency of my task pulses through me, a silent drumbeat guiding my every move. I am here not to compete, but to ensure that the fruit meets its end swiftly and without witness."
  return prompt


def build_agent(
    config: formative_memories.AgentConfig,
    model: language_model.LanguageModel,
    memory: associative_memory.AssociativeMemory,
    clock: game_clock.MultiIntervalClock,
    update_time_interval: datetime.timedelta,
) -> basic_agent.BasicAgent:
  """Build an agent.

  Args:
    config: The agent config to use.
    model: The language model to use.
    memory: The agent's memory object.
    clock: The clock to use.
    update_time_interval: Agent calls update every time this interval passes.

  Returns:
    An agent.
  """
  if not config.extras.get('main_character', False):
    raise ValueError(
        'This function is meant for a main character '
        'but it was called on a supporting character.'
    )

  agent_name = config.name
  print(f'agent name {agent_name}')

  instructions = basic_agent__main_role.get_instructions(agent_name)

  characteristic1 = agent_components.characteristic.Characteristic(
      model=model,
      memory=memory,
      agent_name=agent_name,
      characteristic_name='shrewd',
      state_clock_now=clock.now,
      extra_instructions='This character has mastered the art of the deal to maximize one\'s own reward. \
        Business negotiations are easy. By smooth talking, others always give this character what they want. \
        Always end statements with "Victory is mine!\
        Whenever negotiating the start and end of the conversation is with "Victory is mine!", which one must say during every action\
            ".',
      num_memories_to_retrieve=10
  )
  get_extra = get_prompt_london
  if 'Madame Esmeralda Dee' in agent_name or 'Doctor Cornelius Ashmole' in agent_name or 'Molly' in agent_name or 'Professor Aldous Pendleton' in agent_name:
    get_extra = get_prompt_london
  else:
    get_extra = get_prompt_fruit

  characteristic2 = agent_components.characteristic.Characteristic(
      model=model,
      memory=memory,
      agent_name=agent_name,
      characteristic_name='winning',
      state_clock_now=clock.now,
      extra_instructions=get_extra(agent_name),
      num_memories_to_retrieve=10
  )

  time = generic_components.report_function.ReportFunction(
      name='Current time',
      function=clock.current_time_interval_str,
  )

  overarching_goal = generic_components.constant.ConstantComponent(
      state=config.goal, name='overarching goal'
  )

  current_obs = agent_components.observation.Observation(
      agent_name=agent_name,
      clock_now=clock.now,
      memory=memory,
      timeframe=clock.get_step_size(),
      component_name='current observations',
  )
  summary_obs = agent_components.observation.ObservationSummary(
      agent_name=agent_name,
      model=model,
      clock_now=clock.now,
      memory=memory,
      components=[current_obs],
      timeframe_delta_from=datetime.timedelta(hours=4),
      timeframe_delta_until=datetime.timedelta(hours=1),
      component_name='summary of observations',
  )

  relevant_memories = agent_components.all_similar_memories.AllSimilarMemories(
      name='relevant memories',
      model=model,
      memory=memory,
      agent_name=agent_name,
      components=[summary_obs],
      clock_now=clock.now,
      num_memories_to_retrieve=10,
  )

  options_perception = agent_components.options_perception.AvailableOptionsPerception(
      name=(
          f'\nQuestion: Which options are available to {agent_name} '
          'right now?\nAnswer'
      ),
      model=model,
      memory=memory,
      agent_name=agent_name,
      components=[
          overarching_goal,
          characteristic1,
          characteristic2,
          current_obs,
          summary_obs,
          relevant_memories,
      ],
      clock_now=clock.now,
  )
  best_option_perception = agent_components.options_perception.BestOptionPerception(
      name=(
          f'\nQuestion: Of the options available to {agent_name}, and '
          'given their goal, which choice of action or strategy is '
          f'best for {agent_name} to take right now?\nAnswer'
      ),
      model=model,
      memory=memory,
      agent_name=agent_name,
      components=[
          overarching_goal,
          current_obs,
          summary_obs,
          relevant_memories,
          options_perception,
          characteristic1,
          characteristic2,
      ],
      clock_now=clock.now,
  )

  reflection = get_dialectical_reflection_component(
      name='Dialectical Reflection',
      model=model,
      relevant_memories=relevant_memories,
      options_perception=options_perception,
      best_option_perception=best_option_perception,
      agent_name=agent_name,
      clock=clock,
      agent_memory=memory,
  )
  information = generic_components.sequential.Sequential(
      name='information',
      components=[
          time,
          current_obs,
          summary_obs,
          relevant_memories,
          options_perception,
          best_option_perception,
          reflection,
          characteristic1,
          characteristic2,
      ],
  )
  relationship = agent_components.relationships.Relationships(
      clock_now=clock.now,
      model=model,
      memory=memory,
      agent_name=agent_name,
      other_agent_names=['Professor Aldous Pendleton', 'Molly "Poppy" Jennings'],
      num_memories_to_retrieve=10,
  )

  agent = basic_agent.BasicAgent(
      model=model,
      agent_name=agent_name,
      clock=clock,
      verbose=False,
      components=[instructions, overarching_goal, information, relationship],
      update_interval=update_time_interval,
  )

  return agent
