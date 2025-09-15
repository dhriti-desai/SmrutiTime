from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/smruti')
def smruti():
    today_key = datetime.now().strftime("%m-%d")
    smruti = smruti_memories.get(today_key)
    return render_template('smruti.html', smruti=smruti)


smruti_memories = {
    "06-01": {
        "date": "June 1, 1830",
        "occurrences": [
            "After 49 years on this earth, Parabrahma Purushottam Bhagwan Shri Swaminarayan departed, from Gadhada, on 1 June 1830. To enable all mumukshus to attain the path of moksha, he promised to remain forever present (pragat) on this earth through the Aksharbrahmaswarup Gunatit Satpurush, and first handed over the reins to Aksharbrahma Gunatitanand Swami."
        ],
        "picture": "__"
    },

    "06-03": {
        "date": "June 3, 1971",
        "location": "Sankari, India",
        "occurrences": [
            "In the village of Sankari, Pramukh Swami Maharaj consecrated the marble murtis of Shri Akshar-Purushottam Maharaj and Lakshminarayan Bhagwan on 3 June 1971. This shikkharbaddh mandir was to be the first in a remarkable total of 37 shikkharbaddh mandirs opened by Pramukh Swami Maharaj in India and abroad until his passing in 2016."

        ],
        "picture": "_"
    },

    "06-04": {
        "date": "June 4, 1967",
        "location": "Gondal, India",
        "occurrences": [
            "Yogiji Maharajs Amrut Mahotsav (75th birth anniversary) in Gondal."
        ],
        "picture": "_"
    },

    "06-05": {
        "date": "June 5, 1907",
        "location": "Bochasan, India", 
        "occurrences": [
            "Brahmaswarup Shastriji Maharaj opened the first BAPS mandir by consecrating the murtis of Akshar-Purushottam Maharaj in Bochasan to herald the supreme principle established by Bhagwan Swaminarayan. This marked the formal establishment of BAPS Swaminarayan Sanstha."
        ],
        "picture": "_"
    },

    "06-06": {
        "date": "June 6, 1970",
        "location": "UK",
        "occurrences": [
            "The first visit of the Satpurush to Upcountry in the UK. Yogiji Maharaj travelled from London to Banbury to Leicester to Loughborough to Leicester."

        ],
        "picture": "_"
    },       

    "06-07": {
        "date": "June 7, 2023",
        "location": "London Mandir",
        "occurrences": [
            "The first time such a rangotsav was celebrated in UK & Europe. A special moment when Mahant Swami Maharaj and Pramukh Swami Maharaj both spray coloured water on each other. A celebration of limitless joy and divinity."

        ],
        "picture": "_"
    },       

    "06-08": {
        "date": "June 8, 1974",
        "location": "London, UK",
        "occurrences": [
            "Pramukh Swami Maharaj arrives in London from Zambia on 8 June 1974 as part of his first foreign vicharan as guru of BAPS."

        ],
        "picture": "_"
    },       

    "06-11": {
        "date": "June 11, 2014",
        "location": "Sankari, India",
        "occurrences": [
            "Exactly 11 years ago today, Pujya Mahant Swami writes a historic letter to the BAPS Satsang community announcing that Pramukh Swami Maharaj, at the age of 92, will come to Robbinsville in 2014 to grace the land soon to become home to North America's Swaminarayan Akshardham"
        ],
        "picture": "_"
    },     

    "07-01": {
        "date": "July 1, 2023",
        "location": "Toronto, Canada",
        "occurrences": [
            "On the occasion of Canada Day, Mahant Swami Maharaj stood at the jharukho behind Toronto Mandir an performed aarti with the grand celebration of Canada Day with all the haribhakto."
        ],
        "picture": "_"
    },        

    "07-02": {
        "date": "July 2, 2023",
        "location": "Toronto, Canada",
        "occurrences": [
            "Rajipo Din was celebrated in the presence of His Holiness Mahant Swami Maharaj at the BAPS Shri Swaminarayan Mandir, Toronto, in a wonderful program prepared by the children of BAPS. The program revolved around the idea of making God and the guru happy and earning their grace."
        ],
        "picture": "_"
    },       

    "07-03": {
        "date": "July 3, 2023",
        "location": "Mumbai, India",
        "occurrences": [
            "In Kapolvadi, Mumbai, Yogiji Maharaj initiated Vinu Bhagat as a parshad for the second time in a ceremony in which he initiated eight other youths as parshads."

        ],
        "picture": "_"
    },    


        "07-04": {
        "date": "July 4, 1970",
        "location": "River Thames, London",
        "occurrences": [
            "Yogiji Maharaj bathed Thakorji in the river, which was the first time Thakorji was bathed in a foreign river body."
        ],
        "picture": "_"
    },    


    "07-05": {
        "date": "July 5, 2012",
        "location": "Ahemdabad",
        "occurrences": [
            "In Ahmedabad, Pramukh Swami Maharaj performed the pratishtha ceremony of the murtis for the new shikharbaddh BAPS Swaminarayan Mandir soon to be opened in Nagpur, Maharashtra."

        ],
        "picture": "_"
    },    


    "07-06": {
        "date": "July 6, 1970",
        "location": "Paris",
        "occurrences": [
            "On 7 July 1970, after gracing the UK for 46 days, Yogiji Maharaj departed the UK for India. During a flight stopover at Paris Airport in France, Yogiji Maharaj requested Pujya Pramukh Swami and Pujya Mahant Swami to step foot onto the land of Europe on his behalf, historically marking the first European visit of the Satpurush."
        ],
        "picture": "_"
    },    

    "07-07": {
        "date": "July 7, 2020",
        "location": "Nenpur, India",
        "occurrences": [
            "Mahant Swami Maharaj gifted the Satsang Diksha granth on this day. He wrote a letter to all BAPS devotees and began a parayan on the shastra."
        ],
        "picture": "_"
    },    

    "07-08": {
        "date": "July 8, 2023",
        "location": "Robbinsville, New Jersey",
        "occurrences": [
            "Mahant Swami Maharaj did drashti on BAPS Swaminarayan Akshardham, USA for the first time. Bhagwan Swaminarayan, who looked to the West from Chhapaiya, today saw the Akshardham in which he will forever reside."
        ],
        "picture": "_"
    },    

    "07-09": {
        "date": "July 9, 1911",
        "location": "Junagadh, India",
        "occurrences": [
            "Before the sun rose on that early July morning in Junagadh, Yogiji Maharaj and a group of 7 sadhus departed from the Swaminarayan Mandir in Junagadh to join Shastriji Maharaj in his mission of propagating Akshar-Purushottam upasana."
        ],
        "picture": "_"
    },    

        "07-10": {
        "date": "July 10, 2013",
        "location": "Sarangpur, India",
        "occurrences": [
            "Pramukh Swami Maharaj performed the pratishtha ceremony of the murtis for the new shikharbaddh BAPS Swaminarayan Mandir soon to be opened in Himmatnagar, Gujarat. More than 2,800 devotees from the Sabarkantha region had assembled for the ceremony."
        ],
        "picture": "_"
    },    

    "07-11": {
        "date": "July 11, 2011",
        "location": "Bharuch to India",
        "occurrences": [
            "Pramukh Swami Maharaj sometimes used to take the train as a young child. He had the darshan of Shastriji Maharaj and Yogiji Maharaj at Makarpara station. This train journey was special as Pramukh Swami Maharaj and Mahant Swami Maharaj rode at this station together."
        ],
        "picture": "_"
    },    

        "07-12": {
        "date": "July 12, 1945",
        "location": "Atladara Mandir",
        "occurrences": [
            "Brahmaswarup Shastriji Maharaj opened the fourth such mandir dedicated to Akshar-Purushottam upasana in Atladara, on land sanctified by the auspicious footprints of Bhagwan Swaminarayan."
        ],
        "picture": "_"
    },    

    "07-13": {
        "date": "July 13, 2010",
        "location": "Dehli, India",
        "occurrences": [
            "The new garbhagruh (inner sanctum) of Swaminarayan Akshardham, New Delhi is inaugurated by Pramukh Swami Maharaj."
        ],
        "picture": "_"
    },    

        "07-14": {
        "date": "July 14, 1977",
        "location": "Ashton",
        "occurrences": [
            "Six years after the satsang mandal in Manchester had begun with a handful of devotees, Pramukh Swami Maharaj opened a small mandir in Ashton with the same Murtis that Yogiji Maharaj had originally installed in Islington in 1970."
        ],
        "picture": "_"
    },    

        "07-15": {
        "date": "July 15, 2000",
        "location": "London, UK",
        "occurrences": [
            "A unique celebration in honour of Pramukh Swami Maharaj's guru-bhakti was held at BAPS Shri Swaminarayan Mandir in London in the presence of thousands of devotees."
        ],
        "picture": "_"
    },    

    "07-16": {
        "date": "July 16, 1985",
        "location": "Alexandra Palace Grounds, London, UK",
        "occurrences": [
            "The day on which His Holiness Pramukh Swami Maharaj inaugurated the month-long Cultural Festival of India (CFI)."
        ],
        "picture": "_"
    },    

        "07-17": {
        "date": "July 17, 1980",
        "location": "London, UK"
        "occurrences" [
            "The festival marking the foundation stone-laying ceremony of the new hari mandir in Neasden was celebrated with a grand procession through the local streets of Wembley, North London."
        ],
        "picture": "_"
    },    

    "07-18": {
        "date": "July 18, 1985",
        "location": "London, UK",
        "occurrences": [
            "Pramukh Swami Maharaj's Suvarna Mahotsav where he is weighed against sugar crystals."
    
        ],
        "picture": "_"
    },    

        "07-19": {
        "date": "July 19, 1991",
        "location": "New Jersey, USA",
        "occurrences": [
            "Devotees offered their heartfelt devotion to Guru Pramukh Swami Maharaj during the Platinum Mahotsav on 20 July 1991 in New Jersey, USA."
        ],
        "picture": "_"
    },    

        "07-20": {
        "date": "July 20, 2012",
        "location": "Ahmedabad, India",
        "occurrences": [
            "On Saturday 13 August 2016 at 6.00pm in Sarangpur, Pramukh Swami Maharaj left his physical body and returned to Akshardham. Pujya Swayamprakashdas Swami (Doctor Swami) announced that four years previously, on Friday 20 July 2012, Pramukh Swami Maharaj had written a letter that Pujya Mahant Swami would succeed him as the Guru and President of BAPS."
        ],
        "picture": "_"
    },    

        "07-22": {
        "date": "July 22, 2007",
        "location": "Toronto, Canada",
        "occurrences": [
            "After years of patient, persistent and productive efforts, the first ever shikharbaddh mandir in Canada inaugurated by His Holiness Pramukh Swami Maharaj."
        ],
        "picture": "_"
    },  

}


