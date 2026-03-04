import React, {use} from 'react'
import {createRoot} from "react-dom/client";
import configFile from './config.json'

import {auto_login} from "./user/back-end-connection";
import {get_items} from "./user/back-end-connection";

import type {Item} from "./user/back-end-connection";

const baseURL:string = configFile.baseURL;

interface DataProps {
    username:string
    isLoggedIn:boolean
}

function NotLoggedInPanel() {
    return (
            <div style={{display:'flex', flexDirection:'column', alignItems:'center'}}>
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
            <div style={{display:'flex', flexDirection:'column', alignItems:'center'}}>
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

            <div style={{display:'flex'}}>
                <div style={{display:"flex", alignItems:'center', justifyContent:'center', maxWidth:'200px', flexGrow:'1'}}>
                    <p style={{textAlign:'center'}}>
                        Current user: {username?username:'none'}
                    </p>
                </div>
                <div style={{flexGrow:'1'}}>
                    <h1 style={{textAlign:'center'}}>
                        Main page
                    </h1>
                </div>
                <div style={{display:"flex", alignItems:'center', justifyContent:'center', maxWidth:'200px', flexGrow:'1'}}></div>
            </div>

            <div style={{display:'flex', flexDirection:'column', flexGrow:'1', maxWidth:'600px', marginLeft:'auto', marginRight:'auto', justifyContent:'center'}}>
                <DataDisplay username={username} isLoggedIn={isLoggedIn} />
            </div>

        </div>
    );
}

window.onload = ()=>{
    const rootDiv:HTMLDivElement = document.getElementById("root") as HTMLDivElement
    const root = createRoot(rootDiv);
    root.render(<Main />);
}