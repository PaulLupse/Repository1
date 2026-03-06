import React, {use} from 'react'
import {createRoot} from "react-dom/client";
import configFile from './config.json'

import {auto_login, get_items, logout} from "./user/back-end-connection";

import type {Item} from "./user/back-end-connection";

const baseURL:string = configFile.baseURL;

interface DataProps {
    username:string
    isLoggedIn:boolean
}

function NotLoggedInPanel() {
    return (
            <div id="not_logged_in_panel"
                style={{display:'flex', flexDirection:'column', alignItems:'center', marginTop:'5px', marginBottom:'5px'}}>
                <h3>
                    You are not logged in.
                </h3>
                <a href={baseURL + '/login'}>Login</a>
                <a href={baseURL + '/register'}>Register</a>
            </div>
        )
}

function DataDisplay(props:DataProps) {

    const [itemList, setItemList] = React.useState(Array<Item>);


    React.useEffect(()=> {
                    async function getItems ():Promise<void> {
                        const newItems:Array<Item>|undefined = await get_items();

                        if(newItems) {
                            console.log(newItems);
                            setItemList(newItems);
                        }
                    }
                    if(props.isLoggedIn)
                        getItems();
                },
                [props.isLoggedIn]
            );

    if(props.isLoggedIn) {

        return(
            <div id="display" style={{display:'flex', flexDirection:'column', alignItems:'center', marginTop:'5px', marginBottom:'5px'}}>
                <table>
                    <thead>
                        <tr>
                            <th>
                                Name
                            </th>
                            <th>
                                Value
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {itemList.map(
                            (item:Item, index:number) => {
                                return(
                                    <tr key={index}>
                                        <td>
                                            {item.name}
                                        </td>
                                        <td>
                                            {item.value}
                                        </td>
                                    </tr>
                                );
                            }
                        )}
                    </tbody>
                </table>
            </div>
        );
    }
    else
    {
        return <NotLoggedInPanel />
    }
}

function Main() {

    const [username, setUsername] = React.useState('');
    const [isLoggedIn, setIsLoggedIn] = React.useState(false);

    // folosim un effect pentru a returna utilizatorul curent
    React.useEffect(()=> {
            async function getUser ():Promise<void> {
                const username:string|undefined = await auto_login();
                if(username) {
                    setUsername(username);
                    setIsLoggedIn(true);
                }
            }
            getUser();
        },
        []
    );

    return (
        <div style={{display:"flex", flexDirection:"column", height:'100vh', minWidth:'300px', alignItems:'stretch'}}>

            <div style={{display:'grid', gridTemplateColumns:'1fr auto 1fr', alignItems:'center',
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
                                    if (await logout()) {
                                        setUsername('');
                                        setIsLoggedIn(false);
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
                        Main page
                    </h1>
                </div>
            </div>

            <div style={{display:"flex", justifyContent:'center', height:'100%'}}>
                 <div style={{display:'flex', flexDirection:'column', flexGrow:'1', justifyContent:'center',
                     maxWidth:'600px', }}>
                    <DataDisplay username={username} isLoggedIn={isLoggedIn} />
                </div>

            </div>

        </div>
    );
}

window.onload = ()=>{
    const rootDiv:HTMLDivElement = document.getElementById("root") as HTMLDivElement
    const root = createRoot(rootDiv);
    root.render(<Main />);
}