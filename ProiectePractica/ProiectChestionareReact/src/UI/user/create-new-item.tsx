import React, {useState} from "react";
import {createRoot} from "react-dom/client";
import type {RefObject} from "react";
import {logout, auto_login, add_item} from "./back-end-connection";

import configFile from "../config.json"
import {useNavigate, BrowserRouter} from "react-router-dom";

import type {Item} from "./back-end-connection";

const baseURL:string = configFile.baseURL


class FormQuestion {
    text:string=''
    isOptional:boolean=false
    constructor(text:string, isOptional:boolean) {
        this.text = text;
        this.isOptional = isOptional;
    }
}

class GridQuestion extends FormQuestion {
    isMultipleChoice:boolean=false
    choices:Array<string>=new Array<string>
    constructor(text:string, isOptional:boolean, isMultipleChoice:boolean, choices:Array<string>) {
        super(text, isOptional);
        this.isMultipleChoice = isMultipleChoice;
        this.choices = choices;
    }
}

class TextQuestion extends FormQuestion {
    maxCharacters:number=30

    constructor(text:string, isOptional:boolean, maxChars:number) {
        super(text, isOptional);
        this.maxCharacters = maxChars
    }

}



function CreateNewItem({username}:any) {

    const nameInput:RefObject<HTMLInputElement|null> = React.useRef(null);

    const [formQuestions, setFormQuestions] = useState(Array<TextQuestion|GridQuestion>);

    React.useEffect(
        ()=>{
            setFormQuestions(
            [
                new TextQuestion("Ce vrei ma?", false, 20),
                new TextQuestion("Ce ai ma?", false, 20),
                new TextQuestion("Ce-ti trebe ma?", false, 20),
                new GridQuestion("MilsTespEsg?", false, false, ["Da", "Nu"])
            ]);
        }, []
    )


    return (
        <div style={{display:'flex', flexDirection:'column', justifyContent:"start", alignContent:"center",
                    maxWidth:'600px', flexGrow:'1', gap:'5px', padding:'10px'}}>
                    <input type='text' ref={nameInput} placeholder="Item name" />

                    {
                        formQuestions.map(
                            (question:TextQuestion|GridQuestion, index:number)=> {
                                return(
                                    <div key={index}>
                                        <p>
                                            {index}. {question.text}
                                        </p>
                                        {
                                           (question instanceof TextQuestion)?
                                               <input type='text' maxLength={question.maxCharacters}/>
                                               :
                                               <>
                                                   {
                                                       question.choices.map(
                                                           (choice:string, index:number)=> {
                                                               return (
                                                                   <div key={index} style={{display:'flex', alignItems:'center'}}>
                                                                       <input type='radio' />
                                                                       <p> {index}. {choice}</p>
                                                                   </div>
                                                               )
                                                           }
                                                       )
                                                   }
                                               </>
                                        }
                                    </div>
                                )
                            }
                        )
                    }

                    <button onClick={
                        async() => {

                        }
                    }>
                        Create
                    </button>
        </div>
    )
}

function Main() {

    const [username, setUsername] = React.useState('');
    // isLoggedIn = {-1, daca nu se stie starea de logare; 0, daca nu este logat userul; 1, daca este logat userul}
    const [isLoggedIn, setIsLoggedIn] = React.useState(false);


    const navigate = useNavigate();

    // folosim un effect pentru a returna utilizatorul curent
    React.useEffect(()=> {
            async function getUser ():Promise<void> {
                const username:string|undefined = await auto_login();
                if(username) {
                    setUsername(username);
                    setIsLoggedIn(true);
                }
                else {
                    navigate(baseURL);
                }
            }
            getUser();
        },
        []
    );

    return (
        <div id="Pagina intreaga"
            style={{display:"flex", flexDirection:"column", height:'100vh', minWidth:'300px', alignItems:'stretch',
            gap:'10px'}}>

            <div id="Bara de sus"
                style={{display:'grid', gridTemplateColumns:'1fr auto 1fr', alignItems:'center',
                borderBottom:'5px', borderBottomStyle:'double'}}>

                <div style={{display:"flex", alignItems:'center', gap:'10px', marginLeft:'10px'}}>
                    <p style={{textAlign:'center'}}>
                        Current user: {isLoggedIn?username:'none'}
                    </p>
                    {
                        isLoggedIn &&
                        <button
                            onClick={
                                async()=> {
                                    console.log("Logout button clicked")
                                    if (await logout()) {
                                        setUsername('');
                                        setIsLoggedIn(false);
                                        navigate(baseURL);
                                    }
                                }
                            }
                        >
                            Log out
                        </button>
                    }
                </div>

                <div style={{flexGrow:'1'}}>
                    <h1 style={{textAlign:'center'}}>
                        Create new item
                    </h1>
                </div>

            </div>

            <div id="Continut" style={{display:'flex', alignItems:'center', height:'100%', justifyContent:'center'}}>

                <CreateNewItem username={username}/>

            </div>


        </div>
    );
}

window.onload = () => {
    const rootDiv:HTMLDivElement = document.getElementById("root") as HTMLDivElement
    const root = createRoot(rootDiv);
    root.render(<BrowserRouter><Main /></BrowserRouter>);
}