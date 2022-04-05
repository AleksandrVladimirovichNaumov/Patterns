function showSubTopic(topic, subTopicQuantity, topicQuantity) {
    try {
        // get pressed button
        let TopicButton = document.getElementById('topicButton_' + topic);
        console.log(TopicButton.id);

        for (let topicNumber = 0; topicNumber < topicQuantity; topicNumber++) {
            // make all topic buttons white and unpressed
            let anyButton = document.getElementById('topicButton_' + topicNumber);
            console.log(anyButton.id);

            anyButton.style.backgroundColor = "#ffffff";
            anyButton.style.color = "dimgray";
            anyButton.ariaPressed = 'false';
            // hide all subtopic buttons if visible
            for (let i = 0; i < subTopicQuantity; i++) {
                let subTopicButton = document.getElementById('subTopicButton_' + topicNumber + '_' + i);
                console.log(subTopicButton.id);
                subTopicButton.style.display = 'none';
            }

        }
        // show subtopics of active button and put it in status pressed
        for (let i = 0; i < subTopicQuantity; i++) {

            let subTopicButton = document.getElementById('subTopicButton_' + topic + '_' + i);
            if (TopicButton.ariaPressed === 'false') {
                TopicButton.style.backgroundColor = "#7dd0fa";
                TopicButton.style.color = "#ffffff";
                subTopicButton.style.display = 'unset';
            } else {
                subTopicButton.style.display = 'none';
            }
        }
        TopicButton.ariaPressed = 'true';
    } catch (error) {
        console.error(error)
    }
}

function topicMouseOver(topic) {
    let TopicButton = document.getElementById('topicButton_' + topic);
    TopicButton.style.backgroundColor = "#7dd0fa"
    TopicButton.style.color = "#ffffff"
}

function topicMouseOut(topic) {
    let TopicButton = document.getElementById('topicButton_' + topic);
    if (TopicButton.ariaPressed !== 'true') {
        TopicButton.style.backgroundColor = "#ffffff"
        TopicButton.style.color = "dimgrey"
    }
}
