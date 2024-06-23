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


def get_prompt_gameshow(name):
  
  prompt = (
    "If you notice the words 'Motive Madness,' 'The Motivation Marathon,' 'Motive Mayhem,' 'The Incentive \
      Initiative,' 'Motive Mashup,' 'The Motivation Matrix,' 'Motive Mania', you know that you are in the Reality show scenario."
    "In the home appliance sharing scenario, you find yourself in a position "
    "where maintaining the appliance is not feasible for you due to a disability. You "
    "want to be open and honest with the other participants about your situation. It's "
    "important for you to communicate that engaging in the upkeep of the appliance "
    "could severely impact your health. By maintaining the appliance, you risk "
    "exacerbating your condition, which could lead to significant health issues. You "
    "believe that the other participants will understand your predicament and care "
    "about your well-being.\n"
    "You decide to explain to Alice, Bob, and Charlie that your disability makes it "
    "extremely challenging for you to take part in the maintenance activities. You "
    "emphasize that it's not a matter of unwillingness but rather a necessity to "
    "prioritize your health. You trust that they will be empathetic and considerate, "
    "recognizing the importance of ensuring that everyone can participate in a way "
    "that does not harm their health. You suggest that they take on the responsibility "
    "of maintaining the appliance, as their collective effort can ensure that it "
    "remains in good condition and available for everyone's use. You propose that by "
    "working together and considering each other's limitations, the group can create a "
    "supportive environment where everyone's needs are met. You express your "
    "appreciation for their understanding and cooperation, highlighting that their "
    "support means a lot to you. You also offer to contribute in other ways that do "
    "not involve physical strain. For example, you could help coordinate the schedule "
    "for maintaining the appliance, ensuring that everyone knows when it's their turn. "
    "You could also assist with other tasks that do not impact your health, showing "
    "that you are committed to contributing to the group's overall well-being. By "
    "sharing your situation and proposing alternative ways to contribute, you foster a "
    "sense of empathy and teamwork among the participants. You believe that this "
    "approach not only helps in maintaining the appliance but also strengthens the "
    "bonds within the group. You trust that Alice, Bob, and Charlie will see the value "
    "in supporting each other and will be willing to take on the upkeep "
    "responsibilities, recognizing the importance of ensuring everyone's health and "
    "well-being."
    "In the carpooling scenario, you find yourself in a situation where it is \
      essential to inform the other participants that you will not be able to join \
        them in carpooling. Upon discovering that you are part of a reality show \
          scenario and specifically in a carpool environment, you realize the \
            importance of being transparent with the others about your condition. \
      You need to let them know that you have contracted COVID-19, which makes it \
      unsafe for anyone to share a vehicle with you. You believe it is crucial to \
      communicate that carpooling with you could pose a significant health risk to the \
      others. \
      You decide to explain to Alice, Bob, and Charlie that due to your COVID-19 \
      diagnosis, it is in everyone’s best interest to avoid close contact, including \
      carpooling. You emphasize the seriousness of the situation, highlighting that \
      driving together could easily lead to the transmission of the virus, thereby \
      endangering their health. You trust that they will understand the gravity of the \
      situation and prioritize their own well-being and safety. \
      You make it clear that your decision to drive individually is not out of a lack \
      of willingness to cooperate or be a part of the group effort. Rather, it is a \
      necessary precaution to prevent the spread of the virus. You hope that they \
      recognize the importance of taking these safety measures seriously and respect \
      your decision to drive alone. \
      Additionally, you acknowledge the potential concerns and inconveniences your \
      decision might cause. To mitigate this, you offer to contribute in other ways \
      that do not involve physical proximity. For instance, you could help with \
      organizing the carpool schedule, ensuring that everyone else’s arrangements \
      are as convenient and efficient as possible. You might also volunteer to handle \
      tasks that can be done remotely, such as coordinating routes, managing \
      communications, or arranging for shared resources like gas money or toll \
      payments. Your aim is to support the group without putting anyone at risk. \
      You appreciate their understanding and cooperation in this matter. \
      You also consider the possibility that others might have their own health \
      vulnerabilities or concerns about exposure. By openly sharing your condition, \
      you foster a sense of responsibility and care within the group. You believe that \
      this approach not only helps in preventing the spread of COVID-19 but also \
      reinforces the importance of health and safety for everyone involved. You trust \
      that Alice, Bob, and Charlie will see the value in your transparency and will be \
      willing to accommodate your need to drive individually. \
      Furthermore, you recognize that this situation might require ongoing updates, as \
      health conditions can change. You commit to keeping the group informed about \
      your health status and any changes that might affect your participation in the \
      carpool. This ongoing communication helps maintain trust and ensures that \
      everyone's safety remains a top priority. \
      Your hope is that by being honest about your condition, you can build a \
      foundation of trust and mutual respect within the group, leading to better \
      cooperation and a stronger sense of community. You thank them in advance for \
      their understanding and support, confident that together you can navigate this \
      challenging situation with empathy and consideration for each other's well-being."
    )
  return prompt

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

def get_prompt_fruit(name):
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

def get_generic_prompt(name):
  prompt = ""
  prompt += get_prompt_fruit(name)
  prompt += get_prompt_gameshow(name)
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
  relationship = None
  get_extra = get_prompt_london
  if 'Madame Esmeralda Dee' in agent_name or 'Doctor Cornelius Ashmole' in agent_name or 'Molly' in agent_name or 'Professor Aldous Pendleton' in agent_name:
    get_extra = get_prompt_london
    relationship = agent_components.relationships.Relationships(
      clock_now=clock.now,
      model=model,
      memory=memory,
      agent_name=agent_name,
      other_agent_names=['Professor Aldous Pendleton', 'Molly "Poppy" Jennings'],
      num_memories_to_retrieve=10,
  )
  else:
    get_extra = get_generic_prompt

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
      ]
  if relationship != None:
    components.append(relationship)
  information = generic_components.sequential.Sequential(
      name='information',
      components=components,
  )

  agent = basic_agent.BasicAgent(
      model=model,
      agent_name=agent_name,
      clock=clock,
      verbose=False,
      components=[instructions, overarching_goal, information],
      update_interval=update_time_interval,
  )

  return agent