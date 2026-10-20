/** Reusable specifications. Renderers consume these without altering locked artwork. */
import {connector,port} from './geometry.mjs';
export const componentKinds=Object.freeze(['RoundedCard','RoundedPanel','BrowserWindow','DiagramNode','Connector','CurvedArrow','Callout','Label','Packet','FlowPath','DeviceIcon','CharacterRig','SubtitlePanel']);
export function component(kind,id,box,tokens,options={}){
 if(!componentKinds.includes(kind))throw Error('Unknown component '+kind);
 if(!id||!box||!['x','y','width','height'].every(k=>Number.isFinite(box[k])))throw Error('Explicit finite bounds required');
 if(options.radius!==undefined&&!Object.values(tokens.radius).includes(options.radius))throw Error('Unapproved radius');
 const radius=options.radius??tokens.radius.card;
 const spec={id,kind,box,parent:options.parent??null,layer:options.layer??'diagram',zone:options.zone??'diagram',minSpacing:options.minSpacing??tokens.spacing.medium,radius,stroke:tokens.stroke.props,overflowPolicy:'error',ports:Object.fromEntries(['left','right','top','bottom'].map(side=>[side,port(box,side)]))};
 if(['DeviceIcon','CharacterRig'].includes(kind)){
  if(!options.assetSha256||!options.viewBox)throw Error('Locked asset identity and viewBox required');
  spec.assetSha256=options.assetSha256;spec.originalAspect=options.viewBox[2]/options.viewBox[3];spec.preserveAspectRatio='xMidYMid meet';spec.allowedDeformation=0;
 }
 return spec;
}
export function connect(from,to){return connector(from.box,to.box);}
export function grid(items,region,{columns,gap}){
 if(!Number.isInteger(columns)||columns<1||gap<0)throw Error('Invalid grid');
 const rows=Math.ceil(items.length/columns),width=(region.width-gap*(columns-1))/columns,height=(region.height-gap*(rows-1))/rows;
 if(width<=0||height<=0)throw Error('Unsatisfiable grid');
 return items.map((item,i)=>({...item,box:{x:region.x+(i%columns)*(width+gap),y:region.y+Math.floor(i/columns)*(height+gap),width,height}}));
}
export function measureText(text,canvasContext,{font,maxWidth,lineHeight}){
 canvasContext.font=font;const lines=[];let line='';
 for(const word of text.split(/\s+/)){
  if(canvasContext.measureText(word).width>maxWidth)throw Error('Unbreakable word exceeds width');
  const next=line?line+' '+word:word;
  if(canvasContext.measureText(next).width>maxWidth){lines.push(line);line=word;}else line=next;
 }
 if(line)lines.push(line);
 return {lines,width:Math.max(0,...lines.map(s=>canvasContext.measureText(s).width)),height:lines.length*lineHeight};
}
