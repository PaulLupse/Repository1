import React, { type ReactElement } from "react";

interface Button {
    label:string
};

export default class CustomButton extends React.Component<Button> {
    private label:string;
    constructor(props:Button) {
        super(props);
        this.label = props.label;
    }
    private onClickHandler() {
        console.log("Clocked! " + this.label);
    }
    public render():ReactElement<HTMLButtonElement> {
        return <button value={this.label} onClick={()=>{   
                this.onClickHandler()
            }}/>;
    }
}